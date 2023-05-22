# Use the official Python image as the base image
FROM python:3.10

# Copy the Python script to the working directory
COPY . /app/

# Set the working directory in the container
WORKDIR /app

# Set the entrypoint to the Python script
ENTRYPOINT ["python", "word-count.py"]