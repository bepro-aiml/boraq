# Module 3 - Class 1 Assignment: Data Cleaning

**Khamidullokhon Abduvokhidov**

```python
# Load the Titanic data set for the cleaning practice.
import pandas as pd
import numpy as np
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)
print('Shape:', df.shape)
df.head()

# Count missing values in every column.
df.isnull().sum()

# Replace missing ages with the typical passenger age.
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)
print('Median used:', median_age)
print('Missing Age now:', df['Age'].isnull().sum())

# Fill missing embarkation ports with the most common port.
mode_embarked = df['Embarked'].mode()[0]
df['Embarked'] = df['Embarked'].fillna(mode_embarked)
print('Mode used:', mode_embarked)
print('Missing Embarked:', df['Embarked'].isnull().sum())

# Remove Cabin because most of its values are unavailable.
df = df.drop(columns=['Cabin'])
print('Columns now:', df.shape[1])

# Check whether any full records are duplicated.
print('Duplicates:', df.duplicated().sum())

# Create readable labels for the binary survival outcome.
df['Survived_label'] = df['Survived'].map({0: 'No', 1: 'Yes'})
df[['Survived', 'Survived_label']].head()

# Standardize the sex text by trimming spaces and using lowercase.
df['Sex'] = df['Sex'].str.strip().str.lower()
df['Sex'].value_counts()

# Confirm that the final data set has no missing values.
print('Missing per column:')
print(df.isnull().sum())
print()
print('Final shape:', df.shape)
```
