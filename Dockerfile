FROM python:3.11-slim

# Install system dependencies required for psutil
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# TODO: Fix the following error when running the docker container
# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY ./app .

# Expose port
EXPOSE 5000

# Set Flask environment variables
ENV FLASK_APP=main.py \
    PYTHONUNBUFFERED=1

# Start application
CMD ["python", "main.py"]
