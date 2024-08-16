import os
from mlflow.server import app
from mlflow.server.handlers import initialize_stores
from wsgi_basic_auth import BasicAuth

# Get configuration from environment variables
USERNAME = 'foo'
PASSWORD = 'bar'

application = BasicAuth(app, users={USERNAME: PASSWORD})

if __name__ == "__main__":
    # This block allows running the script directly for testing
    from werkzeug.serving import run_simple

    run_simple("0.0.0.0", 5000, application)