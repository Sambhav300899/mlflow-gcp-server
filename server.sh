#!/bin/bash

# used params from here - https://stackoverflow.com/questions/71687131/how-to-import-mlflow-tracking-server-wsgi-application-via-flask-or-fastapi

export _MLFLOW_SERVER_FILE_STORE=$POSTGRESQL_URL
export _MLFLOW_SERVER_SERVE_ARTIFACTS="true"
export _MLFLOW_SERVER_ARTIFACT_DESTINATION=$STORAGE_URL
export _MLFLOW_SERVER_ARTIFACT_ROOT=$STORAGE_URL
export WSGI_AUTH_CREDENTIALS="${MLFLOW_ID}:${MLFLOW_PASS}"

mlflow db upgrade $POSTGRESQL_URL

exec gunicorn -b "0.0.0.0:5000" wsgi_server:app
