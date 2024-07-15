# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the content of the local frontend directory to the working directory
COPY frontend .

# Install Streamlit
RUN pip install streamlit

# Expose the port where Streamlit runs
EXPOSE 8501

# Command to run Streamlit app
CMD ["streamlit", "run", "frontend.py"]