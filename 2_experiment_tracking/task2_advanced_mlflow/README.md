# **Task 2: Advanced MLflow**

## **Objective**

Create a pipeline that:

1. Runs multiple experiments with different hyperparameters.
2. Logs results to MLflow for comparison.

## **Instructions**

1. **Create a Script to Run Experiments**:
   Write `run_experiments.py` to:
   - Loop through multiple sets of hyperparameters.
   - Train and evaluate models.
   - Log each experiment to MLflow.

2. **Run the Script**:
   Execute the pipeline:

   ```bash
   python run_experiments.py
   ```

3. **Analyze Results:**
    Open the MLflow UI and compare the logged experiments:

   ```bash
   mlflow ui
   ```

## **Expected Output**

- A comparison of models with different hyperparameters.
- Visualizations of metrics and artifact exploration.
