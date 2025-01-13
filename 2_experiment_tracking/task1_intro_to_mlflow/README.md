# **Task 1: Introduction to MLflow**

## **Objective**

Learn how to:

1. Use MLflow to track experiments.
2. Log metrics, parameters, and artifacts.
3. Visualize experiment results in the MLflow UI.

## **Instructions**

1. **Install MLflow**:

   ```bash
   pip install mlflow
   ```

2. **Set Up an Experiment:**
    Create a Python script mlflow_demo.py to:
    * Train a model.
    * Log parameters, metrics, and the trained model.

3. **Run the Script:**
    Execute the script:

    ```bash
    python mlflow_demo.py
    ```

4. **Start the MLflow UI:**
    View your logged experiments:

    ```bash
    mlflow ui
    ```

    Open the UI in your browser at [http://localhost:5000](http://localhost:5000).

## **Expected Output**

* A record of your experiments with parameters, metrics, and artifacts.
* Visualizations of metrics and comparison between runs.