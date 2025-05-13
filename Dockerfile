# Use modern Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only what's needed first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Set environment variables if needed
ENV PYTHONUNBUFFERED=1

# Expose the port
EXPOSE 5000

# Start the Flask app
CMD ["python", "server.py"]

