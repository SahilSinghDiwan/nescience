# ==========================================================
# NESCIENCE — Investigation Notes loader (NESC-13)
#
# [006] INVESTIGATION NOTES is the archive's methodology drawer: how this
# investigation works, what it accepts as evidence, and why it is built to
# stop at UNKNOWN rather than past it. It is *public* — the method is part
# of the exhibit's argument, not backstage material.
#
# Notes are hand-authored markdown committed under docs/notes/, mirroring
# how docs/bibliography.md already works: version-controlled, no storage
# layer, no write path, no auth. This module reads that directory, parses a
# small `key: value` header off the top of each file, and renders a
# deliberately narrow subset of markdown to HTML.
#
# The renderer is hand-rolled on purpose. The exhibit ships with one
# dependency (Flask) and no network assets; pulling in a markdown library
# to format five essays is not a trade worth making. The subset below is
# the subset the notes actually use — if a note needs more, widen this
# rather than reaching for a package.
# ==========================================================

import html
import os
import re

NOTES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs", "notes")

# Header keys a note may declare. Anything else in the header block is
# ignored rather than silently rendered into the body.
_HEADER_KEYS = {"title", "number", "summary", "status"}


# ----------------------------------------------------------
# Parsing
# ----------------------------------------------------------

def _split_header(text):
    """Peel a leading `key: value` block off a note.

    The header runs from the first line until the first blank line, and only
    while every line still looks like `key: value`. A note with no header is
    all body — the loader falls back to the filename for a title."""
    lines = text.splitlines()
    header, cursor = {}, 0
    for line in lines:
        if not line.strip():
            cursor += 1
            break
        match = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not match:
            break
        key = match.group(1).strip().lower()
        if key not in _HEADER_KEYS:
            break
        header[key] = match.group(2).strip()
        cursor += 1
    return header, "\n".join(lines[cursor:]).strip()


def _inline(text):
    """Inline markdown -> HTML, on already-escaped text.

    Escaping happens first, so no authored note can inject markup; the
    patterns below then reintroduce only the tags we chose to support."""
    text = html.escape(text)
    # `code` before everything else, so emphasis inside code is left alone.
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)
    # [label](target) — internal/relative links only. An authored note has no
    # business pointing at an external host: the exhibit makes no network
    # calls, and a live outbound link in the methodology drawer would be the
    # one exception that breaks that promise.
    def _link(match):
        label, target = match.group(1), match.group(2)
        if not target.startswith(("/", "#")):
            return label
        return f'<a href="{target}">{label}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _link, text)


def render_markdown(text):
    """The supported subset: h2/h3, paragraphs, unordered lists, blockquotes,
    horizontal rules, and the inline marks above. Blocks are separated by
    blank lines."""
    out = []
    for block in re.split(r"\n\s*\n", text.strip()):
        block = block.strip()
        if not block:
            continue
        lines = block.splitlines()

        if re.match(r"^-{3,}$", block):
            out.append('<hr class="rule">')
        elif block.startswith("### "):
            out.append(f"<h3>{_inline(block[4:].strip())}</h3>")
        elif block.startswith("## "):
            out.append(f"<h2>{_inline(block[3:].strip())}</h2>")
        elif block.startswith("# "):
            # A single leading h1 is the note's own title, which the template
            # already renders — demote it so the page keeps one h1.
            out.append(f"<h2>{_inline(block[2:].strip())}</h2>")
        elif lines[0].startswith(("- ", "* ")):
            # A list item may wrap across lines; a continuation line is any
            # line that doesn't open a new bullet, and folds into the item
            # above it.
            items = []
            for line in lines:
                stripped = line.strip()
                if stripped.startswith(("- ", "* ")):
                    items.append(stripped[2:].strip())
                elif items:
                    items[-1] = f"{items[-1]} {stripped}"
            rendered = "".join(f"<li>{_inline(item)}</li>" for item in items)
            out.append(f"<ul>{rendered}</ul>")
        elif all(line.startswith(">") for line in lines):
            quoted = " ".join(line.lstrip("> ").strip() for line in lines)
            out.append(f"<blockquote>{_inline(quoted)}</blockquote>")
        else:
            out.append(f"<p>{_inline(' '.join(line.strip() for line in lines))}</p>")
    return "\n".join(out)


# ----------------------------------------------------------
# Loading
# ----------------------------------------------------------

def _slug_from_filename(filename):
    """`001-what-counts-as-evidence.md` -> `what-counts-as-evidence`."""
    stem = os.path.splitext(filename)[0]
    return re.sub(r"^\d+[-_]", "", stem)


def _load_file(filename):
    path = os.path.join(NOTES_DIR, filename)
    with open(path, "r", encoding="utf-8") as handle:
        header, body = _split_header(handle.read())

    slug = _slug_from_filename(filename)
    number = header.get("number") or re.match(r"^(\d+)", filename)
    if hasattr(number, "group"):
        number = number.group(1)
    return {
        "slug": slug,
        "number": (number or "").zfill(3) if number else "",
        "title": header.get("title") or slug.replace("-", " ").title(),
        "summary": header.get("summary", ""),
        "status": header.get("status", ""),
        "body_html": render_markdown(body),
    }


def all_notes():
    """Every note on file, ordered by filename (the numeric prefix is the
    reading order, not the authoring date — these are methodology notes,
    not a chronological log)."""
    if not os.path.isdir(NOTES_DIR):
        return []
    filenames = sorted(f for f in os.listdir(NOTES_DIR) if f.endswith(".md"))
    return [_load_file(f) for f in filenames]


def get(slug):
    """One note by slug, or None if there is no such note on file."""
    return next((note for note in all_notes() if note["slug"] == slug), None)
