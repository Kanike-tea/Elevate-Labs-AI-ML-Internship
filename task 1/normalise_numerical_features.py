import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Titanic-Dataset.csv')

scaler = StandardScaler()
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch']

df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

print(df.head())
