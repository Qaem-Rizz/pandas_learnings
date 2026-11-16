# Pandas primarily revolves around TWO data structures:
# 1. Series
# 2. DataFrame
# Let's understand them.


"""Series = One-dimensional labelled data.
One-dimensional means it has only ONE dimension. Think of it as a single list of values with labels."""

import pandas as pd

purchases = pd.Series([5000, 3000, 7000, 2000])

print(purchases) #Something interesting will happen. Where did 0, 1, 2, 3 come from? Pandas automatically created labels called "Index".

#Can we create our own Index? Absolutely:
purchases = pd.Series([5000, 3000, 7000],index=["Rahul", "Aman", "Sara"])

print(purchases)


# pd.Series() is a Pandas constructor. A constructor is simply something used to create an object.

# Here:
# - pd → Pandas library.
# - Series() → Creates a Series.
# - [30000, 40000, 50000, 60000] → Data we're providing.
# - print() → Displays the result.
# Notice dtype: int64.

# This tells us that Pandas has stored these values as 64-bit integers.

#-------------------------------------------------------------------------------

"""
DataFrame = Two-dimensional labelled data structure containing rows and columns. Think of it as an Excel spreadsheet.
A DataFrame can contain different data types in different columns."""

import pandas as pd

data = {
    "Customer": ["Rahul", "Aman", "Sara"],
    "Purchase": [5000, 3000, 7000],
    "City": ["Delhi", "Patna", "Mumbai"]
}

df = pd.DataFrame(data)

df.index = ["A", "B", "C"] #changing the indexes again..

print(df)



#------------------------------------------------------------------------
#DATA TYPES:

# Common Pandas data types:
# Data Type	                       Meaning	                         Example
# int64	                        Integer numbers	                       25
# float64	                     Decimal numbers	                  25.5
# object	          General Python objects, commonly strings	     Rahul
# bool	                           True/False	                      True
# datetime64	                  Date and time	                    2026-11-16
# category	                    Categorical data	              IT, HR, Finance
# string	                  Dedicated string data type	          Rahul



#How to check the data type?
#For an individual Series:

print(df["Purchase"].dtype)


#for whole Dataframe:
print(df.dtypes)
