import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# Step 1: Dataset load karo
df = pd.read_csv('train.csv')

# Step 2: Dataset ka basic info check karo
print("Dataset Info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Step 3: Missing values ko handle karo
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
df.drop(columns=['Cabin'], inplace=True)

# Step 4: Duplicate rows hatao
df.drop_duplicates(inplace=True)

# Step 5: Encoding karo categorical columns ka
df = pd.get_dummies(df, columns=['Sex', 'Embarked'])

# Step 6: Normalize/standardize karo numeric features
scaler = StandardScaler()
df[['Age', 'Fare']] = scaler.fit_transform(df[['Age', 'Fare']])

# Step 7: Outliers detect aur remove karo (Fare column ke liye)
Q1 = df['Fare'].quantile(0.25)
Q3 = df['Fare'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
df = df[(df['Fare'] >= lower_bound) & (df['Fare'] <= upper_bound)]

# Optional: Boxplot dikhao (visual check)
plt.figure(figsize=(8,4))
sns.boxplot(df['Fare'])
plt.title('Fare Outlier Visualization')
plt.show()

# Step 8: Cleaned data save karo
df.to_csv('cleaned_titanic.csv', index=False)
print("Cleaned data saved to cleaned_titanic.csv")
