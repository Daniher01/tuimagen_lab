# app/Dockerfile
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY app/tuimagen_lab/Pipfile app/tuimagen_lab/Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy project
COPY ./app/tuimagen_lab /app/

# # Collect static files
# RUN mkdir -p /app/staticfiles
# RUN pipenv run python manage.py collectstatic --noinput

# Run the application with Gunicorn and create superuser
CMD pipenv run python manage.py migrate && \
    pipenv run python create_superuser.py && \
    pipenv run gunicorn tuimagen_lab.wsgi:application --bind 0.0.0.0:8000

EXPOSE 8000