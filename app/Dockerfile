# app/Dockerfile
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY tuimagen_lab/Pipfile tuimagen_lab/Pipfile.lock /app/
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Copy project
COPY ./tuimagen_lab /app/

# # Collect static files
# RUN mkdir -p /app/staticfiles
# RUN pipenv run python manage.py collectstatic --noinput

# Run the application
CMD pipenv run python manage.py migrate && pipenv run python manage.py runserver 0.0.0.0:8000

EXPOSE 8000