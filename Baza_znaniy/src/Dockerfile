FROM python:3.11-slim

# Install uv (fast Python package installer)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="$UV_PROJECT_ENVIRONMENT/bin:$PATH"

WORKDIR /app

# Copy only the files needed for dependencies first
COPY pyproject.toml ./

# Install dependencies using uv into the virtual environment
RUN uv venv /opt/venv && \
    uv pip install -e .

# Copy the rest of the application
COPY . .

# Expose the application port
EXPOSE 8000

# Run alembic migrations on startup and then start the uvicorn server
CMD ["sh", "-c", "uv run alembic upgrade head && uv run uvicorn main:app --host 0.0.0.0 --port 8000"]
