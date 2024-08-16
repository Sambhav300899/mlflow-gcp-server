import os 
import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# Generate random data
np.random.seed(42)
X = np.random.rand(100, 1)
y = 3 * X.squeeze() + 2 + np.random.randn(100) * 0.5

############## Set MLflow tracking URI ##############
os.environ["MLFLOW_TRACKING_USERNAME"] = "foo"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "bar"

mlflow.set_tracking_uri("https://mlflow-runner-pxqwrkeeca-uc.a.run.app")
#####################################################

# Split the data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start an MLflow run
with mlflow.start_run():
    model = LinearRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    mlflow.log_param("fit_intercept", model.fit_intercept)
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    mlflow.sklearn.log_model(model, "linear_regression_model")

    print(f"Model saved in run {mlflow.active_run().info.run_id}")
    print(f"MSE: {mse}")
    print(f"R2: {r2}")

