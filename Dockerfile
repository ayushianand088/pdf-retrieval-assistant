# Use Python 3.12 devcontainer base
FROM mcr.microsoft.com/devcontainers/python:3.12

# Ensure output is flushed
ENV PYTHONUNBUFFERED=1

# Install dependencies required by your app
RUN apt-get update && apt-get install -y curl poppler-utils

# Set working directory
WORKDIR /workspace/pdf-retrieval-assistant

# Copy requirements first (better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy the whole project into container
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI with Uvicorn (looking into app/main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]