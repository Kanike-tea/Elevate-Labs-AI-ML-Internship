import pandas as pd
df = pd.read_csv('/Users/kanike/Documents/ai&ml internship/Elevate-Labs-AI-ML-Internship/task 1/Titanic-Dataset.csv')

# For numerical features: Age, Fare
df['Age'] = df['Age'].fillna(df['Age'].median())
df['Fare'] = df['Fare'].fillna(df['Fare'].median())

# For categorical features: Cabin, Embarked
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop columns with too many missing values
df.drop(columns=['Cabin'], inplace=True)

print(df.head())