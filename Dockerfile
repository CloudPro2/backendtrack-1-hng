# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=app.py

# Expose the port that the app runs on
EXPOSE 5173

# Run the application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5173"]
