import os
from wsgi_basic_auth import BasicAuth
from mlflow.server import app as mlflow_app

app = BasicAuth(mlflow_app)

if __name__ == "__main__":
    # This block allows running the script directly for testing
    from werkzeug.serving import run_simple

    run_simple("0.0.0.0", 5000, app)