import os
from mlflow.server import app
from mlflow.server.handlers import initialize_backend_stores
from wsgi_basic_auth import BasicAuth

# Get configuration from environment variables
# DB_URL = os.environ.get('POSTGRESQL_URL', None)
# ARTIFACT_ROOT = os.environ.get('STORAGE_URL', "/tmp/mlruns")
# # Initialize the backend stores
# # initialize_backend_stores(DB_URL, ARTIFACT_ROOT, None)

# # Set the MLflow tracking URI
# app.config['MLFLOW_TRACKING_URI'] = DB_URL

# # Set the default artifact root
# app.config['MLFLOW_ARTIFACT_ROOT'] = ARTIFACT_ROOT

# # Set the app name
# app.config['MLFLOW_APP_NAME'] = "basic-auth"

application = BasicAuth(app, users={"foo": "bar"})

if __name__ == "__main__":
    # This block allows running the script directly for testing
    from werkzeug.serving import run_simple

    run_simple("0.0.0.0", 5000, application)