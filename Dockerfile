FROM python:3.7-slim-stretch

LABEL \
Name=django_sample \
Version=19.0.1 \
Maintainer='Saurabh Rautela<saurabh@rautela.dev>'

ENV PYTHONUNBUFFERED=1
ENV PYTHONBREAKPOINT=0

RUN groupadd -r 1000 \
&& useradd --no-log-init -r -g 1000 1000

COPY ./requirements.txt /app/dev/

WORKDIR /app/dev

RUN apt-get update \
&& apt-get install -y python-dev \
libpq-dev \
build-essential \
&& pip install -r requirements.txt \
&& apt-get remove --purge python-dev \
libpq-dev \
build-essential -y \
&& apt-get autoremove -y \
&& rm -rf /var/lib/apt/lists/*

COPY ./dev /app/dev

COPY ./tools/docker/runserver_entrypoint.sh /app/tools/docker/runserver_entrypoint.sh

COPY ./tools/docker/migration_entrypoint.sh /app/tools/docker/migration_entrypoint.sh

WORKDIR /app/dev/sample

ENTRYPOINT ["/app/tools/docker/runserver_entrypoint.sh"]
