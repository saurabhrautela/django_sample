FROM python:3.7.2-slim-stretch

LABEL \
Name=django_docker_boilerplate \
Version=0.0.1 \
Maintainer='Saurabh Rautela<saurabhrautela@pm.me>'

COPY ./requirements.txt /app/dev/

WORKDIR /app/dev

RUN apt-get update \
&& apt-get install -y curl \
&& pip install -r requirements.txt \
&& rm -rf /var/lib/apt/lists/*

COPY ./dev /app/dev

# Copy entrypoint scripts
COPY ./tools/docker/runserver_entrypoint.sh /app/tools/docker/runserver_entrypoint.sh

COPY ./tools/docker/migration_entrypoint.sh /app/tools/docker/migration_entrypoint.sh

WORKDIR /app/dev/sample

ENTRYPOINT ["/app/tools/docker/runserver_entrypoint.sh"]
