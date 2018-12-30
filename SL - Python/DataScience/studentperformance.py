import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("StudentsPerformance.csv")

print("<-----Data PreProcessing----->")
print("\nHead and Description of Dataset")
print(df.head(5))
print(df.describe())
print(df.info())

print("\nRemoving unwanted columns")
df1 = df.drop(['lunch','test preparation course'], axis=1)
print(df1.head(5))

print("\nFilling empty values")
df['parental level of education'] = df['parental level of education'].fillna("bachelor's degree")
print(df.head(5))

print("\nMapping values/attributes in race/ethnicity to types")
df['race/ethnicity'] = df['race/ethnicity'].map({'group A':'Asian Students','group B':'African Students','group C':'Afro-Asian Students','group D':'American Students','group E':'European Students'})
print(df.head(5))


print("\n")
print("<-------Data Visualisation------->")
print(pd.crosstab(df.gender,df['test preparation course']))

ax = sns.countplot(data=df,x='gender',hue='race/ethnicity',palette='Set1')
ax.set(title='Male and Female belonging to each group',xlabel='Gender',ylabel='Count')
plt.show()

interval = (0,40,60,75,100)
category = ['Failed','Second Class','First Class','Distinction']
df['grade_math']  = pd.cut(df['math score'],interval,labels=category)
ax = sns.countplot(data=df,x='grade_math',hue=df['grade_math'],palette='Set1')
ax.set(title='Math Grades',xlabel='Grade Category',ylabel='Count')
plt.show()

df['grade_reading']  = pd.cut(df['reading score'],interval,labels=category)
ax = sns.countplot(data=df,x='grade_reading',hue=df.grade_reading,palette='Set2')
ax.set(title='Reading Grades',xlabel='Grade Category',ylabel='Count')
plt.show()

df['grade_writing']  = pd.cut(df['writing score'],interval,labels=category)
ax = sns.countplot(data=df,x='grade_writing',hue=df['grade_writing'],palette='Set3')
ax.set(title='Writing Grades',xlabel='Grade Category',ylabel='Count')
plt.show()
