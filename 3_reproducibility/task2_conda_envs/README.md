# **Task 2: Conda Environments**

## **Objective**

Learn how to:

1. Create a reproducible Conda environment.
2. Share and recreate environments using `environment.yml`.

## **Instructions**

1. **Set Up a Conda Environment**:
   Create a new environment:

   ```bash
   conda create -n reproducibility-env python=3.9 -y
   conda activate reproducibility-env
   ```

2. **Install Dependencies:**
    Install the required packages:

    ```bash
    pip install scikit-learn==1.0 numpy==1.21
    ```

3. **Export the Environment:**
    Save the environment configuration:

    ```bash
    conda env export --no-builds > environment.yml
    ```

4. **Recreate the Environment:**
    Share the environment.yml file. Others can recreate the same environment using:

    ```bash
    conda env create -f environment.yml
    conda activate reproducibility-env
    ```

## **Expected Output**

* A fully reproducible environment with the exact dependencies listed in environment.yml.
