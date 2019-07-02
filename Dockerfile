FROM python:3.7-slim-stretch

LABEL \
Name=django_sample \
Version=19.0.1 \
Maintainer='Saurabh Rautela<saurabh@rautela.dev>'

ENV PYTHONUNBUFFERED=1
ENV PYTHONBREAKPOINT=0

COPY ./requirements.txt /app/dev/

WORKDIR /app/dev

RUN apt-get update \
&& apt-get install -y python-dev \
libpq-dev \
build-essential \
&& pip install -r requirements.txt \
&& apt-get remove --purge python-dev \
build-essential -y \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/*

COPY ./dev /app/dev

COPY ./config/docker/runserver_entrypoint.sh /app/config/docker/runserver_entrypoint.sh

COPY ./config/docker/migration_entrypoint.sh /app/config/docker/migration_entrypoint.sh

WORKDIR /app/dev/sample

ENTRYPOINT ["/app/config/docker/runserver_entrypoint.sh"]
