# Use the official Python base image from Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PATH="/usr/local/bin:$PATH"

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install system dependencies for PostgreSQL, or add your DB client if needed
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the project files into the container
COPY . /app/

# Set environment variables for Django settings (adjust if needed)
ENV DJANGO_SETTINGS_MODULE=myproject.settings

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django app with Gunicorn (adjust the command for your app)
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

