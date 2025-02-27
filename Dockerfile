# Use official Python slim image
FROM python:3.12-slim

# Set environment variables and install Poetry
ENV PATH="/root/.local/bin:$PATH"

RUN pip install poetry

# Set working directory
WORKDIR /app

# Copy Poetry files and install dependencies (without dev dependencies)
COPY pyproject.toml poetry.lock* /app/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the project files
COPY . /app

# Expose the application port
EXPOSE 8000

# Run the application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]