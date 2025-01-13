import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import itertools

# Generate synthetic dataset
X, y = make_regression(n_samples=1000, n_features=10, noise=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Set up hyperparameter grid
param_grid = {
    "n_estimators": [50, 100, 150],
    "max_depth": [3, 5, 7]
}

# Run experiments
mlflow.set_experiment("Hyperparameter Tuning Experiment")
for params in itertools.product(*param_grid.values()):
    param_dict = dict(zip(param_grid.keys(), params))
    with mlflow.start_run():
        # Log parameters
        mlflow.log_params(param_dict)

        # Train model
        model = RandomForestRegressor(**param_dict)
        model.fit(X_train, y_train)

        # Evaluate model
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mlflow.log_metric("mse", mse)

        # Log the model
        mlflow.sklearn.log_model(model, "model")

        print(f"Params: {param_dict}, MSE: {mse}")