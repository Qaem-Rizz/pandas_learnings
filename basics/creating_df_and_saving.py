import pandas as pd


#making a dataframe using dictionary in python:
data = {
    "Name" : ['abdullah', 'sharjeel', 'tabish', 'zama','hamed'],
    "Age": [22,23,23,19,23],
    "City": ['patna', 'bagalore', 'patna', 'patna', 'hyderabad']
}


#passing that dictionary under the pd.dataframe  function to convert it
df = pd.DataFrame(data)

print(df)


#to further save it in CSV:

#df.to_csv("output.csv" , index=False) #here the INDEX false will spare us unnecesary indexing


#saving in excel file:
df.to_excel("output.xlsx" , index = False)


#saving in json:
df.to_json("output.json" , index = False)