# Dockerfile for the E-commerce Service (Django + Gunicorn)

# Use an official Python runtime as a parent image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt /app/requirements.txt

#Update pip
RUN pip install --upgrade pip
# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the application code into the container
COPY . /app

# Expose the port the app runs on
EXPOSE 8000

# Run the gunicorn server with the Django application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ecommerce.wsgi:application", "--workers=3"]





RUN pip install -r requirements.txt

# wsgi:application"]
