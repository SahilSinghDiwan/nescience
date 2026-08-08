# ==========================================================
# NESCIENCE — participant identity & consent model
#
# Real testimony is personal, so the exhibit keeps a hard line
# between what an investigator (owner-side) may see and what a
# public surface may render:
#
#   private  -> the participant's real name, their name->code
#               mapping, unpublished responses, recorded timestamp
#   public   -> an anonymised CODE + the responses they opted to
#               publish, nothing else
#
# The private identity fields live alongside the recorded timestamp
# inside each record's "Case File" block. The public projection drops
# that block wholesale and re-surfaces only the code, so a private
# field can never leak by being forgotten in a template.
#
# See NESC-01. Kept intentionally dependency-light: this module works
# on plain interview records (the same dicts database.py stores) so it
# never has to reach into Flask or the matcher.
# ==========================================================

CASE_FILE_KEY = "Case File"

# Keys stored inside the Case File block. "Recorded" is written by app.py;
# the rest are the private identity/consent fields this module owns.
RECORDED_KEY = "Recorded"
NAME_KEY = "Name"
CODE_KEY = "Code"
PUBLISHED_KEY = "Published"

# Fallback code when a name yields no usable letters, and the pad
# character used to reach two letters for very short names.
FALLBACK_CODE = "XX"
PAD_CHAR = "X"


# ----------------------------------------------------------
# Code generation
# ----------------------------------------------------------

def code_from_name(name):
    """Return the two-letter base code for a real name, uppercased.

    The code is the first two *letters* of the name — non-letter leading
    characters (digits, punctuation, spaces) are skipped so '_bob' and
    '7-eleven' still produce sensible codes. Fallbacks:
      - fewer than two letters -> padded with 'X' ('A' -> 'AX')
      - no letters / empty / missing -> 'XX'
    """
    letters = [ch for ch in str(name or "") if ch.isalpha()]
    if not letters:
        return FALLBACK_CODE
    base = "".join(letters[:2]).upper()
    return (base + PAD_CHAR)[:2]  # pad single-letter names to length two


def collect_codes(records):
    """The set of codes already assigned across every record (published
    or not) — codes are globally unique, so publication state is ignored
    here."""
    codes = set()
    for record in records:
        code = get_code(record)
        if code:
            codes.add(code)
    return codes


def assign_code(name, records):
    """Pick a unique code for a new record given the records that already
    exist. On collision with an existing code we append the smallest
    unused integer, per base code: 'AL', then 'AL1', 'AL2', ...

    Existing codes are read from `records`, so this must be called with
    the records present *before* the new one is appended.
    """
    base = code_from_name(name)
    taken = collect_codes(records)
    if base not in taken:
        return base
    suffix = 1
    while f"{base}{suffix}" in taken:
        suffix += 1
    return f"{base}{suffix}"


# ----------------------------------------------------------
# Reading / writing identity on a record
# ----------------------------------------------------------

def _case_file(record):
    """The record's Case File block, or an empty dict for legacy records
    that predate it. Read-only — never mutates the record."""
    block = record.get(CASE_FILE_KEY, {})
    return block if isinstance(block, dict) else {}


def get_name(record):
    """The participant's real name, or None if not recorded (private)."""
    return _case_file(record).get(NAME_KEY)


def get_code(record):
    """The record's assigned code, or None if it has not been assigned
    (e.g. a legacy participants.json entry)."""
    return _case_file(record).get(CODE_KEY)


def is_published(record):
    """Whether the participant opted to publish. Missing/legacy records
    are treated as unpublished."""
    return bool(_case_file(record).get(PUBLISHED_KEY, False))


def apply_identity(record, name, published, records):
    """Stamp a new record with its private identity: assign a code from
    the existing `records`, then store name/code/published in the Case
    File block. Returns the assigned code.

    `records` must be the records that exist *before* this one is added.
    """
    code = assign_code(name, records)
    block = record.setdefault(CASE_FILE_KEY, {})
    block[NAME_KEY] = name
    block[CODE_KEY] = code
    block[PUBLISHED_KEY] = bool(published)
    return code


def ensure_code(record, records):
    """Lazily backfill a code for a legacy record that has a name but no
    code yet (needed only when such a record must be displayed). Records
    that already have a code are returned unchanged.
    """
    existing = get_code(record)
    if existing:
        return existing
    code = assign_code(get_name(record), records)
    record.setdefault(CASE_FILE_KEY, {})[CODE_KEY] = code
    return code


# ----------------------------------------------------------
# Projections
# ----------------------------------------------------------

def public_projection(records):
    """Return the public-safe view of the archive: only *published*
    records, each reduced to its code plus the responses.

    The private Case File block (real name, code mapping, publication
    flag, recorded timestamp) is dropped entirely; the code is the only
    identity that survives. This is the single helper public surfaces
    should use — they never touch raw records.
    """
    public = []
    for record in records:
        if not is_published(record):
            continue
        responses = {
            module: answers
            for module, answers in record.items()
            if module != CASE_FILE_KEY
        }
        public.append({"code": get_code(record), "responses": responses})
    return public


def name_code_mapping(records):
    """Private accessor: the real-name -> code mapping across all records
    (published or not). For the investigator surface only — never expose
    this on a public route. Records without a name are skipped.
    """
    mapping = {}
    for record in records:
        name = get_name(record)
        code = get_code(record)
        if name and code:
            mapping[name] = code
    return mapping
