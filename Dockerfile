# Use the official Python image from the Docker Hub
FROM python:3.12.6-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_DEBUG=1

# Expose the port that the Flask app runs on
EXPOSE 5000

# Run the Flask application
CMD ["flask", "run"]