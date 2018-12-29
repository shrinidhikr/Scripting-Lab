import pandas as pd
data = pd.read_json('employee.json')
print ("----Printing the dataframe----\n", data)
print ("----Printing 0,1,2,3 records of the dataframe----\n",data[0:4]['Salary'])
print ("----Printing Salary and Name Columns of the dataframe----\n", data.loc[:,['Salary','Name']])
print ("----Printing 1st, 3rd and 5th row of the dataframe----\n", data.loc[[1,3,5],['Salary', 'Name']])
print("----Combining different column values as one record ----\n",data.to_json(orient='records', lines=True))

print("---writing the screen output into an excel file called printmeout.xls---\n")
with open('printmeout.xls', 'w+') as f:
  print(data, file = f)
