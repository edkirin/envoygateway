FROM python:3.10-slim

ARG INTERNAL_PORT
ARG WORKERS

ENV \
    DOCKER_CONTAINER Yes \
    INTERNAL_PORT ${INTERNAL_PORT} \
    WORKERS ${WORKERS} \
    PYTHONDONTWRITEBYTECODE 1 \
    PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./service /app/service
COPY requirements.txt /app
COPY run.sh /app

RUN \
    pip install --upgrade pip && \
    pip install -r /app/requirements.txt

EXPOSE $INTERNAL_PORT

ENTRYPOINT [ "/app/run.sh" ]
