# Stage 1: Build stage
FROM python:3.9-slim AS build-stage

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY app.py .

# Stage 2: Final stage
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only the necessary files from build stage
COPY --from=build-stage /app /app

# Expose the port Flask app will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
