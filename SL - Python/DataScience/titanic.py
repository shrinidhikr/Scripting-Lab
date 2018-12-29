import pandas as pd
from pandas import Series, DataFrame

# numpy, matplotlib, seaborn
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# get titanic & test csv files as a pandas DataFrame
titanic_df = pd.read_csv("train.csv")

# preview the data
print("======Data Headers=======")
titanic_df.head()

print("=====Data Decription=====")
# column description
titanic_df.info()
titanic_df.describe()


# drop unnecessary columns, these columns won't be useful in analysis and prediction
titanic_df = titanic_df.drop(['PassengerId', 'Name', 'Ticket'], axis=1)

# Another way of dropping columns done in place, that is a new variable is not required.
titanic_df.drop(['Parch'], axis=1, inplace=True)

print("=====Check if columns were really dropped=====")
# print dataframe again to see how the contents look like
titanic_df.head()

# Next look for columns which have missing values. Fill those cells with some sort of default value(should be similar to other values in the colums)

titanic_df["Embarked"] = titanic_df["Embarked"].fillna("S")
# Check if there are no missing values
print(titanic_df["Embarked"])

'''
Now you perform visualization
'''

# 1 Survival based on sex

titanic_df[["Sex", "Survived"]].groupby(
    ['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False)


def get_person(passenger):
    age, sex = passenger
    return 'child' if age < 16 else sex


titanic_df['Person'] = titanic_df[['Age', 'Sex']].apply(get_person, axis=1)

# No need to use Sex column since we created Person column
titanic_df.drop(['Sex'], axis=1, inplace=True)


# create dummy variables for Person column, & drop Male as it has the lowest average of survived passengers
person_dummies_titanic = pd.get_dummies(titanic_df['Person'])
person_dummies_titanic.columns = ['Child', 'Female', 'Male']
person_dummies_titanic.drop(['Male'], axis=1, inplace=True)

titanic_df = titanic_df.join(person_dummies_titanic)
fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(10, 5))

sns.factorplot('Person', data=titanic_df, kind='count', ax=axis1)

# average of survived for each Person(male, female, or child)
person_perc = titanic_df[["Person", "Survived"]].groupby(
    ['Person'], as_index=False).mean()
sns.barplot(x='Person', y='Survived', data=person_perc,
            ax=axis2, order=['male', 'female', 'child'])

plt.show()
titanic_df.drop(['Person'], axis=1, inplace=True)

'''End of #1 '''


'''No of passedngers in each group '''


facet = sns.FacetGrid(titanic_df, hue="Survived",aspect=4)
facet.map(sns.kdeplot,'Age',shade= True)
facet.set(xlim=(0, titanic_df['Age'].max()))
facet.add_legend()

# Pclass

# sns.factorplot('Pclass',data=titanic_df,kind='count',order=[1,2,3])
sns.factorplot('Pclass', 'Survived', order=[1, 2, 3], data=titanic_df, size=5)

# create dummy variables for Pclass column, & drop 3rd class as it has the lowest average of survived passengers
pclass_dummies_titanic = pd.get_dummies(titanic_df['Pclass'])
pclass_dummies_titanic.columns = ['Class_1', 'Class_2', 'Class_3']
pclass_dummies_titanic.drop(['Class_3'], axis=1, inplace=True)

titanic_df.drop(['Pclass'], axis=1, inplace=True)
titanic_df = titanic_df.join(pclass_dummies_titanic)

plt.show()

'''End of pclass'''
