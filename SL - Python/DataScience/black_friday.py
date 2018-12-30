import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("BlackFriday.csv")

print("<-----Data PreProcessing----->")
print("\nHead and Description of Dataset")
print(df.head(5))
print(df.describe())
print(df.info())

print("\nRemoving unwanted columns")
df.drop(['User_ID','Product_ID','Stay_In_Current_City_Years'], axis=1, inplace=True)
print(df.head(5))

print("\nFilling empty values")
df['City_Category'] = df['City_Category'].fillna("A")
print(df.head(5))

print("\nMapping values/attributes in City_Category to types")
df['City_Category'] = df['City_Category'].map({'A':'Metro cities','B':'Small Towns','C':'Villages'})
print(df.head(5))

print("\nRenaming the column names")
df.rename(columns={'Product_Category_1':'Baseball_Caps','Product_Category_2':'Wine_Tumblers','Product_Category_3':'Pet_Raincoats'},inplace=True)
print(df.head(5))

print("\nMapping values/attributes in Marital Status to types")
df['Marital_Status'] = df['Marital_Status'].map({1:'Married',0:'Un-Married'})
print(df.head(5))


print("\n")
print("<-------Data Visualisation------->")
print(pd.crosstab(df.Gender,df.Baseball_Caps))
print(pd.crosstab(df.Gender,df.Wine_Tumblers))

ax = sns.countplot(data=df,x='Gender',hue='City_Category',palette='Set1')
ax.set(title='Male and Female belonging to each city',xlabel='Gender',ylabel='Count')
plt.show()

