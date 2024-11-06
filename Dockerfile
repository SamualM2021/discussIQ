# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Command to run FastAPI or Flask depending on the environment variable
CMD ["sh", "-c", "if [ \"$APP_FRAMEWORK\" = \"fastapi\" ]; then uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000; else flask run --host=0.0.0.0 --port 8000; fi"]
