import pandas as pd
import pickle
from sklearn.metrics import mean_squared_error
import json

# Load test data
test = pd.read_csv("data/processed.csv")

# Load model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Evaluate the model
X = test[["x1", "x2"]]
y_true = test["y"]
y_pred = model.predict(X)
mse = mean_squared_error(y_true, y_pred)

# Save metrics
with open("metrics.json", "w") as f:
    json.dump({"mse": mse}, f)