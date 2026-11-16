import pandas as pd

df = pd.read_csv("ecommerce_pandas_practice.csv" , encoding="utf-8")
#df stands for dataframe (we took it as a varibale name here only) , and pd.read_csv is a function to read data from a csv file.
#sometimes, the encodings gets messed up and the data cant be loaded, the fix is to make the encoding explicitly declared by hand as we did- 2 types are there... UTF-8 and "latin1"




print(df)

#for reading from EXCEL:
df2 = pd.read_excel("SampleSuperstore.xlsx")
print(df2)

#for reading from json:
df3 = pd.read_json("sample_Data.json")

print(df3)