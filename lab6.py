import pandas as pd

df = pd.read_csv("Titanic-Dataset.csv")

p_survived = len(df[df['Survived'] == 1]) / len(df)
p_not_survived = len(df[df['Survived'] == 0]) / len(df)

p_female_survived = len(df[(df['Sex'] == 'female') & (df['Survived'] == 1)]) / len(df[df["Survived"] == 1])
p_female_not_survived = len(df[(df['Sex'] == 'female') &(df['Survived'] == 0)]) / len(df[df["Survived"] == 0])

survived_prob = p_survived * p_female_survived
not_survived = p_not_survived * p_female_not_survived

if survived_prob > not_survived:
    print("Prediction: Survived")
else:
    print("Prediction: Not Survived")

