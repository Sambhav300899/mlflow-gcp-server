#!/bin/bash
# mlflow server \
# -h 0.0.0.0 \
# -p 5000 \
# --backend-store-uri $POSTGRESQL_URL \
# --default-artifact-root $STORAGE_URL \
# --app-name basic-auth

# mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri $POSTGRESQL_URL --default-artifact-root $STORAGE_URL
export _MLFLOW_SERVER_ARTIFACT_ROOT=$POSTGRESQL_URL
export _MLFLOW_SERVER_FILE_STORE=$STORAGE_URL

exec gunicorn --bind 0.0.0.0:5000 -w 4 wsgi_server:app
