# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY backend/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the content of the local backend directory to the working directory
COPY backend .

# Command to run the backend API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
