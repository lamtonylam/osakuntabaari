# syntax=docker/dockerfile:1
FROM python:3.12-slim-bookworm

# --- Runtime env: faster startup, cleaner logs, no .pyc writes ---
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PIP_NO_CACHE_DIR=1

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# 1. Install deps FIRST (cached unless pyproject/uv.lock change).
#    --frozen: assert lockfile is up to date; --no-dev: skip dev deps;
#    --no-cache: don't bloat the image with uv's HTTP cache.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-cache

# 2. Copy only what the app needs (keeps image small, build context lean).
COPY src ./src
COPY templates ./templates

# Drop root: no perf cost, safer on shared hosts.
RUN useradd --create-home --uid 10001 appuser \
    && chown -R appuser:appuser /app
USER 10001

# App listens on 8000 (see src/main.py). Expose must match.
EXPOSE 8000

# Run the venv's uvicorn directly — NOT `uv run` (which re-resolves
# the project on every container start: slower boot + extra memory).
# Single worker = minimal RAM/CPU for this tiny service. Bump
# --workers only if you see CPU saturation under load.
CMD [".venv/bin/uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1", "--no-access-log"]
