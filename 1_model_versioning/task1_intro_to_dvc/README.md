# **Task 1: Introduction to DVC**

## **Objective**

Learn how to:

1. Initialize DVC in a Git project.
2. Track datasets with DVC.
3. Update datasets and manage versions.

## **Instructions**

1. **Initialize a Git Repository**:

    ```bash
    git init
    ```

2. **Initialize DVC:**

    ```bash
    dvc init
    git add .dvc .gitignore
    git commit -m "Initialize DVC"
    ```

3. **Add a Dataset:**

    Create a folder called data and a sample dataset:

    ```bash
    mkdir data
    echo "sepal_length,sepal_width,petal_length,petal_width,species
    5.1,3.5,1.4,0.2,setosa
    4.9,3.0,1.4,0.2,setosa
    6.2,3.4,5.4,2.3,virginica" > data/iris.csv
    ```

    Track the dataset with DVC:

    ```bash
    dvc add data/iris.csv
    git add data/.gitignore data/iris.csv.dvc
    git commit -m "Track iris dataset with DVC"
    ```

4. **Update the Dataset:**

    Modify data/iris.csv by appending:

    ```bash
    echo "5.7,2.8,4.1,1.3,versicolor" >> data/iris.csv
    ```

    Re-track it:

    ```bash
    dvc add data/iris.csv
    git add data/iris.csv.dvc
    git commit -m "Update dataset with new samples"
    ```

5. **Restore the Dataset:**

    Simulate deleting the dataset:

    ```bash
    rm data/iris.csv
    ```

    Restore it using DVC:

    ```bash
    dvc checkout
    ```

6. **Check Status:**

    Use dvc status to see the current state of tracked files.

## **Expected Output**

* A .dvc file (iris.csv.dvc) in your repository.
* Ability to restore datasets and track their changes systematically.
