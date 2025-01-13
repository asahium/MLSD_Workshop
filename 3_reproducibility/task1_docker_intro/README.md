# **Task 1: Introduction to Docker**

## **Objective**

Learn how to:

1. Create a Dockerfile for a simple ML project.
2. Build and run a Docker container.
3. Ensure reproducibility using a containerized environment.

## **Instructions**

1. **Create a Training Script**:
   Write a simple Python script `train.py` that trains a dummy model:

   ```python
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
   ```

2. **Create a Requirements File:**
    List the required dependencies in requirements.txt:

    ```test
    scikit-learn==1.0
    numpy==1.21
    ```

3. **Write a Dockerfile:**
    Create a Dockerfile to containerize the environment:

    ```dockerfile
    FROM python:3.9-slim

    # Set working directory
    WORKDIR /app

    # Copy and install dependencies
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy project files
    COPY . .

    # Define default command
    CMD ["python", "train.py"]
    ```

4. **Build the Docker Image:**
    Build an image for your project:

    ```bash
    docker build -t reproducibility-docker .
    ```

5. **Run the Docker Container:**
    Execute the training script in a container:

    ```bash
    docker run reproducibility-docker
    ```

6. **Verify Reproducibility:**

    * Ensure that the environment and model outputs are consistent across multiple runs.
    * Share the Dockerfile with others to reproduce the same results.

## **Expected Output:**

* A trained model saved as model.pkl inside the container.
* Reproducibility of the environment and outputs.
