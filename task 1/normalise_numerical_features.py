import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('/Users/kanike/Documents/ai&ml internship/Elevate-Labs-AI-ML-Internship/task 1/Titanic-Dataset.csv')

scaler = StandardScaler()
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch']

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print(df.head())