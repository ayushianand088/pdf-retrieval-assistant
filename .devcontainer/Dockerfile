FROM mcr.microsoft.com/devcontainers/python:3.12

ENV PYTHONUNBUFFERED=1

RUN sudo apt-get update && sudo apt-get install -y curl

# Copy requirements first
COPY ../requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install --no-cache-dir -r /tmp/requirements.txt

# Copy project files
COPY ../ /workspace/pdf-retrieval-assistant

# Set working directory to your app folder
WORKDIR /workspace/pdf-retrieval-assistant/app

# Expose FastAPI port
EXPOSE 8000

# Run Uvicorn inside the app folder
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]