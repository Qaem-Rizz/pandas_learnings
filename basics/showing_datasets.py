# Real job mein tumhe aksar koi CSV/Excel file milegi aur tumhe kuch nahi pata hoga ki uske andar kya hai.

# Tumhara first reaction ye nahi hona chahiye:
# "Chalo analysis start karte hain."

# Pehle dataset ko inspect karna hai.



#------------------------------------------------------------------------
#(1)- head() — Starting Rows Dekhna . default value me first 5 rows dikhata hai , otherwise HEAD(N) for N rows..
#------------------------------------------------------------------------


import pandas as pd
import numpy as np

data = {
    "Name": ["Rahul", "Aman", "Sara", "Ali", "Priya"],
    "Age": [23, 25,np.nan , 26, 22],
    "Salary": [30000, 40000, 50000, 60000, 35000],
    "Department": ["IT", "HR", "IT", "Finance", "HR"]
}

df = pd.DataFrame(data)

print(df.head(2))

#------------------------------------------------------------------------
#(2) - tail() — Last Rows Dekhna. by default ye bhi last 5 rows dikhata hai...
#------------------------------------------------------------------------
print("\n--------------------------------------------------------")
print(df.tail(2))




#------------------------------------------------------------------------
#(3) - SHAPE — Dataset Kitna Bada Hai?
#------------------------------------------------------------------------
#example: (5,5) - What does (5, 5) mean? First number = rows ; Second number = columns...similar to how shape used to work in numpy
print("\n--------------------------------------------------------")
print(df.shape)

#------------------------------------------------------------------------
#(4) - COLUMNS — Column Names display krta hai, we can also display the names in LIST form by adding .tolist()
#------------------------------------------------------------------------
print("\n--------------------------------------------------------")

print(df.columns.tolist())

#------------------------------------------------------------------------
#(5) - INDEX — Row Labels
#------------------------------------------------------------------------

#example output : RangeIndex(start=0, stop=5, step=1) ... shows that starts from 0 and goes upto 4... so total 5 rows are there..
print("\n--------------------------------------------------------")

print(df.index)

#------------------------------------------------------------------------
#(6) - SIZE : total number of elements/cells
#------------------------------------------------------------------------
print("\n--------------------------------------------------------")
print(df.size)


#------------------------------------------------------------------------
#(7) - NDIM : number of dimensions. 1 for a series, 2 for Dataframe obv.
#------------------------------------------------------------------------
print("\n--------------------------------------------------------")
print(df.ndim)



#------------------------------------------------------------------------
#(8) - INFO: This gives you a summary of the entire DataFrame...sbkchhh
#------------------------------------------------------------------------
print("\n--------------------------------------------------------")

print(df.info())


#in the output of this ... you'll see Non-Null Count. This is very important:
# Suppose:
# Name
# 5 non-null

# There are 5 rows and all 5 have a value.

# But suppose:
# Salary
# 4 non-null

# There are 5 rows but only 4 Salary values.

# Therefore:

# 1 value is missing.



print("\n--------------------------------------------------------")
#------------------------------------------------------------------------
# (9) - DESCRIBE: This gives statistical information about numeric columns.
#------------------------------------------------------------------------
print(df.describe())

#important output observations:
# count: Number of non-missing values.

# mean:Average.

# std:Standard deviation. This tells us roughly how spread out the values are from the mean.

# 50%: This is the median.


# REMEMBER: describe() mostly summarizes numeric columns.

# So it won't give you useful statistical summaries for others because those are categorical/textual.

# But you can ask Pandas to describe all columns:
print("\n--------------------------------------------")
print(df.describe(include="all"))



#------------------------------------------------------------------------------
#(10) - value_counts() — What's Inside a Column? Suppose we want to know How many employees belong to each department?
#------------------------------------------------------------------------------

# syntax: df["column_name"].value_counts()

print("\n--------------------------------------------")
print(df["Department"].value_counts())

#-----------------------------------------------------------
#(11) - UNIQUE: Is column ke andar different values kya-kya hain?
#-----------------------------------------------------------

print("\n--------------------------------------------")

print(df["Department"].unique())


# "nunique" means number of unique values :
print("\n--------------------------------------------")
print(df["Department"].nunique())

#-----------------------------------------------------------------------


# df.columns
# df.index
# df.size
# df.ndim
# df.dtypes
# df.shape
# these are all attributes and not functions



# but, 
# df.head()
# df.tail()
# df.info()
# df.describe()
# are methods/functions, so they use ().