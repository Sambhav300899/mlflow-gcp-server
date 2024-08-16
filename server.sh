#!/bin/bash
# mlflow server \
# -h 0.0.0.0 \
# -p 5000 \
# --backend-store-uri $POSTGRESQL_URL \
# --default-artifact-root $STORAGE_URL \
# --app-name basic-auth

# mlflow server -h 0.0.0.0 -p 5000 --backend-store-uri $POSTGRESQL_URL --default-artifact-root $STORAGE_URL

# exec gunicorn --bind 0.0.0.0:5000 -w 4 wsgi_server:app

export _MLFLOW_SERVER_FILE_STORE=$POSTGRESQL_URL
export _MLFLOW_SERVER_SERVE_ARTIFACTS="true"
export _MLFLOW_SERVER_ARTIFACT_DESTINATION=$STORAGE_URL
export _MLFLOW_SERVER_ARTIFACT_ROOT=$STORAGE_URL
export WSGI_AUTH_CREDENTIALS="foo:bar"

exec gunicorn -b "0.0.0.0:5000" wsgi_server:app
