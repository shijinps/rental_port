# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables to avoid writing .pyc files and to run Django in production mode
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt (make sure to create it before building the Docker image)
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose port 8000 for the Django development server
EXPOSE 8000

# Run Django migrations and start the server
CMD ["bash", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
