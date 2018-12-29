import pandas as pd
data = pd.read_csv('employee.csv')
print (data)
# Slice the result for first 5 rows
print (data[0:5]['salary'])
# Use the multi-axes indexing funtion
print (data.loc[:,['salary','name']])
# Use the multi-axes indexing funtion
print (data.loc[[1,3,5],['salary','name']])
# Use the multi-axes indexing funtion
print (data.loc[2:6,['salary','name']])
