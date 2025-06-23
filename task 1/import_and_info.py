import pandas as pd

# Load dataset
df = pd.read_csv('/Users/kanike/Documents/ai&ml internship/Elevate-Labs-AI-ML-Internship/task 1/Titanic-Dataset.csv')

# Basic information
print(df.info())

# Check for null values
print(df.isnull().sum())

# Preview data
print(df.head())
