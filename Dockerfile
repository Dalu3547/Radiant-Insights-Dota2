# Use a small Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your exporter script into the container
COPY custom_exporter.py .

# Install required Python libraries
RUN pip install --no-cache-dir prometheus_client requests

# Expose the port used by Prometheus
EXPOSE 9000

# Run the exporter
CMD ["python", "custom_exporter.py"]
