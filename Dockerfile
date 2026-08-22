# ==========================================================
# NESCIENCE — container image for the exhibit
#
# The exhibit is deliberately self-contained: one dependency
# (Flask) and every asset committed under static/. That makes
# the image small and the build fully offline after pip.
# ==========================================================

FROM python:3.12-slim

# Don't write .pyc files, don't buffer stdout — logs should appear
# as the request is served, not when the buffer happens to flush.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /exhibit

# Dependencies first, so editing the exhibit doesn't re-run pip.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# Collected testimony is personal (brief §11a). Keep it on a volume
# rather than baked into the image, and never in a layer.
VOLUME ["/exhibit/data"]
ENV NESCIENCE_DATA_DIR=/exhibit/data

EXPOSE 5001

# gunicorn rather than the dev server: the dev server prints a warning
# about exactly this and is single-threaded.
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "2", "--access-logfile", "-", "app:app"]
