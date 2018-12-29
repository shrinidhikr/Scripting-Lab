import pandas as pd
from pandas import Series, DataFrame

# get titanic & test csv files as a pandas DataFrame
iris_df = pd.read_csv("iris.csv")
print("......Printing the IRIS DataFrame completely.....")
print(iris_df)
print(".............Printing the Info.....")
iris_df.info()
print("........Describing.....")
iris_df.describe()
print(".............Printing using dataframe functions.....")
print (iris_df[["Class", "Sepal_Length"]].groupby(
    ['Class'], as_index=False).mean())

print("The maximum sepal length is",iris_df['Sepal_Length'].max())
