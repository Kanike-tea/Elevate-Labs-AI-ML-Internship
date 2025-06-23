import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/kanike/Documents/ai&ml internship/Elevate-Labs-AI-ML-Internship/task 1/Titanic-Dataset.csv')
numerical_cols = ['Age', 'Fare', 'SibSp', 'Parch']

# Boxplot before removing outliers
for col in numerical_cols:
    plt.figure(figsize=(5, 2))
    sns.boxplot(x=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()

# Remove outliers using IQR
for col in numerical_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df = df[(df[col] >= lower) & (df[col] <= upper)]
    
print(df.shape)
print(df.head())