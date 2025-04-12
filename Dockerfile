# Use an official Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .

# Expose the port the app runs on
EXPOSE 8000

# Run the FastAPI app
CMD ["python", "main.py"]
