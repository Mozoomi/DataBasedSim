import pandas as pd

filePath = str(input("File Path: "))
df = pd.read_csv(filePath)

df = df.dropna()

#columns
columns = int(input("How many columns to drop: "))
for i in range(columns):
   column_name = input("Name of Column: ")
   df = df.drop(column_name, axis=1)
   print("Column Removed")
   
#rows
rowsDeleteNum = int(input("How many column's rows to delete: "))
if rowsDeleteNum > 0:
   column_name = input("Name of Row's Column: ")

for i in range(rowsDeleteNum):
   row_value = input("Name of Column's Row: ")

   df = df[df[column_name] != row_value]
   print("Row Removed")

df.to_csv(filePath, index=False)