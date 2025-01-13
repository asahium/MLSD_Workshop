# **Task 2: Advanced DVC Pipelines**

## **Objective**

Create and run a DVC pipeline that includes:

1. Preprocessing a dataset.
2. Training a machine learning model.
3. Evaluating the model.

## **Instructions**

1. **Create a Dataset**:
   Save a raw dataset in `data/raw.csv`:

   ```bash
   mkdir -p data
   echo "x1,x2,y
   1,2,3
   4,5,9
   7,8,15" > data/raw.csv
   ```

2. **Create a Preprocessing Script:**

    Write a script pipeline/preprocess.py that splits the dataset into training and test sets.

3. **Create a Training Script:**

    Write a script pipeline/train.py that trains a simple model.

4. **Create an Evaluation Script:**

    Write a script pipeline/evaluate.py to calculate and log model performance.

5. **Create a DVC Pipeline:**

    Link these steps into a DVC pipeline using dvc.yaml:

    ```yaml
    stages:
        preprocess:
            cmd: python pipeline/preprocess.py
            deps:
            - pipeline/preprocess.py
            - data/raw.csv
            outs:
            - data/processed.csv

        train:
            cmd: python pipeline/train.py
            deps:
            - pipeline/train.py
            - data/processed.csv
            outs:
            - models/model.pkl

        evaluate:
            cmd: python pipeline/evaluate.py
            deps:
            - pipeline/evaluate.py
            - models/model.pkl
            outs:
            - metrics.json
    ```

6. **Run the Pipeline:**

    ```bash
    dvc repro
    ```

7. **Commit the Pipeline:**

    ```bash
    git add dvc.yaml .gitignore
    git commit -m "Create DVC pipeline"
    ```

## **Expected Output**

* A fully functional pipeline tracked by DVC.
* Outputs like data/processed.csv, models/model.pkl, and metrics.json.