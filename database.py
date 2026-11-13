import contextlib
import datetime
import fcntl
import json
import os
import shutil
import tempfile

# Collected testimony is personal (brief §11a), so where it is written has to
# be movable: in the container it belongs on a mounted volume, never in an
# image layer. NESCIENCE_DATA_DIR overrides the location; unset, it stays
# exactly where it has always been, beside the code.
_DATA_DIR = os.environ.get("NESCIENCE_DATA_DIR") or os.path.dirname(
    os.path.abspath(__file__)
)
FILE_NAME = os.path.join(_DATA_DIR, "participants.json")


class StoreCorruptError(RuntimeError):
    """participants.json exists but cannot be parsed as a list of records.

    The damaged file is left in place (a copy is kept aside); nothing is
    ever written over it, because treating it as empty would erase every
    testimony it still holds."""


def _parse(text):
    if not text.strip():
        return []
    data = json.loads(text)
    if not isinstance(data, list):
        raise ValueError("expected a JSON list")
    return data


def load_interviews():
    """Return every saved interview as a list (empty if none/corrupt).

    Reads never modify the file. Writers replace it atomically, so a reader
    always sees a complete version and needs no lock. A damaged file reads
    as empty here, but save_interview() refuses to write over it."""
    try:
        with open(FILE_NAME, "r") as file:
            return _parse(file.read())
    except FileNotFoundError:
        return []
    except ValueError:
        return []


@contextlib.contextmanager
def _exclusive_lock():
    """Serialise writers across threads and gunicorn worker processes."""
    with open(FILE_NAME + ".lock", "a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(lock, fcntl.LOCK_UN)


def save_interview(interview_data, prepare=None):
    """Append one interview and return its index.

    The read-modify-write happens under an exclusive file lock and the new
    file is written to a temp file in the same directory, then renamed into
    place, so a crash can never leave a half-written archive.

    `prepare(existing)`, if given, is called under the lock with the records
    that exist before this one, so anything derived from them (a participant
    code, the case index) cannot collide with a concurrent submission.

    Raises StoreCorruptError, after keeping the damaged file aside, if the
    existing file cannot be parsed."""
    with _exclusive_lock():
        try:
            with open(FILE_NAME, "r") as file:
                text = file.read()
        except FileNotFoundError:
            text = ""
        try:
            interviews = _parse(text)
        except ValueError as exc:
            stamp = datetime.datetime.now().strftime("%Y%m%dT%H%M%S%f")
            aside = f"{FILE_NAME}.corrupt-{stamp}"
            shutil.copy2(FILE_NAME, aside)
            raise StoreCorruptError(
                f"{FILE_NAME} could not be parsed; left untouched, copy kept "
                f"at {aside}"
            ) from exc

        if prepare is not None:
            prepare(interviews)
        index = len(interviews)
        interviews.append(interview_data)

        fd, tmp = tempfile.mkstemp(
            dir=os.path.dirname(FILE_NAME), prefix=".participants-", suffix=".tmp"
        )
        try:
            with os.fdopen(fd, "w") as out:
                json.dump(interviews, out, indent=4)
                out.flush()
                os.fsync(out.fileno())
            os.replace(tmp, FILE_NAME)
        except BaseException:
            if os.path.exists(tmp):
                os.unlink(tmp)
            raise
    return index
