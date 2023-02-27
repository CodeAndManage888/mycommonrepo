import pandas as pd

excel_workbook = 'sample.xlsx'
df = pd.read_excel(excel_workbook)

print(df)

for column in df.columns:
 df[column] = df[column].str.replace(r'\w',"")
print(df)

df.to_excel("new_file.xlsx")









