import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load training data
train = pd.read_csv("data/processed.csv")

# Train a linear regression model
model = LinearRegression()
X = train[["x1", "x2"]]
y = train["y"]
model.fit(X, y)

# Save the model
with open("models/model.pkl", "wb") as f:
    pickle.dump(model, f)