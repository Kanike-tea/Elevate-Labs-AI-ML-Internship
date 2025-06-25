import pandas as pd

# Load dataset
df = pd.read_csv('Titanic-Dataset.csv')

# Basic information
print(df.info())

# Check for null values
print(df.isnull().sum())

# Preview data
print(df.head())
