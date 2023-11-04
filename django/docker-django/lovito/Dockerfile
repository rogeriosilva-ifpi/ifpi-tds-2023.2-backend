FROM python:3.11.6-slim-bullseye as base

WORKDIR /home/app/

# Python specific settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Dependences
COPY ./requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r ./requirements.txt

# Copying Project Files
COPY . .

EXPOSE 8000

# Dev Stage
FROM base as development
# OBS. RENDER: Não tem supor a multistage, incluir comando abaixo na interface web
# Docker Command python manage.py runserver 0.0.0.0:8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Prod Stage
FROM base as production

RUN pip install gunicorn

