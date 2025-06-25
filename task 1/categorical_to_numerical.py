import pandas as pd
df = pd.read_csv('Titanic-Dataset.csv')

# Convert 'Sex' and 'Embarked' into numeric
df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

# You may also drop Name, Ticket (non-numeric/unique text)
df.drop(columns=['Name', 'Ticket'], inplace=True)

print(df.head())
