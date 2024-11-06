# Dockerfile Containerization Guide

## Overview
This document explains the **Dockerfile** setup for containerizing your Python application, which supports both **FastAPI** and **Flask** frameworks. Docker ensures that your application runs consistently across different environments, making it easy to deploy and scale.

## Dockerfile Structure

### 1. **Base Image**
We begin by using an official Python image as the base. This ensures we have a Python environment with necessary dependencies pre-installed.

```dockerfile
  FROM python:3.11-slim
```
- A minimal Python image based on Debian, reducing unnecessary overhead while providing a Python runtime.

### 2. **Set Working Directory**
```dockerfile
  WORKDIR /app
```
- We set the /app directory inside the container as the working directory. This is where all the app’s code will reside.

### 3. **Copy Requirements**
```dockerfile
  COPY requirements.txt /app/
```
- Next, we copy the requirements.txt file to /app inside the container. This file lists the Python dependencies necessary for the application.

### 4. **Install Dependencies**
```dockerfile
  RUN pip install --no-cache-dir -r requirements.txt
```
- We install the dependencies specified in the requirements.txt using pip. The --no-cache-dir option prevents unnecessary caching, keeping the image smaller.

### 5. **Copy Application Code**
```dockerfile
  COPY . /app/
```
- We copy all the application code into the container’s /app directory. This includes the Flask and FastAPI app code, static files, templates, etc.

### 5. **Expose Application Port**
```dockerfile
  EXPOSE 8000
```
By default, both FastAPI and Flask apps run on port 8000. We expose this port so that the app is accessible when the container is running.

### 8. **Run the Application**
```dockerfile
  CMD ["sh", "-c", "if [ \"$APP_FRAMEWORK\" = \"fastapi\" ]; then uvicorn fastapi_app.main:app --host 0.0.0.0 --port 8000; else flask run --host=0.0.0.0 --port 8000; fi"]
```
The CMD instruction determines which framework (FastAPI or Flask) to run based on the environment variable APP_FRAMEWORK.

FastAPI: Runs with uvicorn, using the fastapi_app.main:app entry point.
Flask: Runs with the Flask development server, using flask run.

### 2. **Environment Variable**
```dockerfile
  docker run -e APP_FRAMEWORK=fastapi <image_name>  # For FastAPI
  docker run -e APP_FRAMEWORK=flask <image_name>    # For Flask
```
To switch between FastAPI and Flask, set the APP_FRAMEWORK environment variable when running the container:

# Building the Docker Image
1. Build the Docker image using the following command
docker build -t <image_name> .
2. Run the container specifying the framework
docker run -e APP_FRAMEWORK=fastapi <image_name>
# or
docker run -e APP_FRAMEWORK=flask <image_name>

