from sklearn.linear_model import LinearRegression
import numpy as np
import pickle

# Dummy dataset
X = np.random.rand(100, 1)
y = 3 * X + np.random.rand(100, 1)

# Train model
model = LinearRegression()
model.fit(X, y)

# Save the model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")