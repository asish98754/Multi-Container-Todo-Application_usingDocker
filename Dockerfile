# Use Python base image
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY api/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask API port
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
