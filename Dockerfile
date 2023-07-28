FROM python:3.9

# Set environment variables for Python buffering and disable bytecode generation
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Set the working directory inside the container
WORKDIR /app


# Copy the Django project code into the container
COPY backend/ /app/

# Set the working directory to the Django project directory
WORKDIR /app/backend


# Expose the port on which the Django application will run (change this if your Django app uses a different port)
EXPOSE 8000

# Run Django's development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]