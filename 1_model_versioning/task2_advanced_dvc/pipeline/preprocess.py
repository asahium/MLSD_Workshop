import pandas as pd
from sklearn.model_selection import train_test_split

# Load raw data
data = pd.read_csv("data/raw.csv")

# Split into training and test sets
train, test = train_test_split(data, test_size=0.2, random_state=42)

# Save processed data
train.to_csv("data/processed.csv", index=False)