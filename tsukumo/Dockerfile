# Start with a Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code and install dependencies
COPY app/ /app
COPY requirements.txt /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
