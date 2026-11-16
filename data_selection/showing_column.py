# Your manager asks:
# 1. Show only employee names.
# 2. Show only salaries.
# 3. Show Name and Salary together.
# 4. Show Rahul's complete record.
# 5. Show employees with index 0, 2 and 4...etc
# This is called Data Selection.
import pandas as pd

data = {
    "Order_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    
    "Customer": [
        "Rahul", "Aman", "Sara", "Ali", "Priya",
        "Rahul", "Zoya", "Aman", "Kabir", "Sara"
    ],
    
    "Age": [23, 25, 24, 26, 22, 23, 27, 25, 29, 24],
    
    "City": [
        "Delhi", "Patna", "Mumbai", "Lucknow", "Delhi",
        "Mumbai", "Patna", "Delhi", "Lucknow", "Mumbai"
    ],
    
    "Product": [
        "Laptop", "Mouse", "Keyboard", "Laptop", "Monitor",
        "Mouse", "Laptop", "Keyboard", "Monitor", "Laptop"
    ],
    
    "Category": [
        "Electronics", "Accessories", "Accessories", "Electronics",
        "Electronics", "Accessories", "Electronics", "Accessories",
        "Electronics", "Electronics"
    ],
    
    "Quantity": [1, 2, 1, 1, 2, 3, 1, 2, 1, 1],
    
    "Price": [50000, 500, 1500, 55000, 12000,
              500, 52000, 1500, 13000, 51000],
    
    "Payment_Mode": [
        "UPI", "Card", "UPI", "Cash", "Card",
        "UPI", "Card", "Cash", "UPI", "Card"
    ],
    
    "Order_Status": [
        "Delivered", "Delivered", "Pending", "Delivered",
        "Cancelled", "Delivered", "Pending", "Delivered",
        "Cancelled", "Delivered"
    ]
}

df = pd.DataFrame(data)

#-------------------------------------------------
# 1. Selecting a Single Column
#-------------------------------------------------
# Suppose you only want employee names from column "NAME".

print(df["Customer"]) 
#also returns the dtype.
#Selecting one column using single square brackets generally returns a Series.



#-------------------------------------
# 2. Selecting Multiple Columns
#-------------------------------------

# Now suppose your manager wants:
# - Employee Name
# - Salary
# - Department
print("\n---------------------------------------------")
print(df[["Customer", "City"]]) #passing column names within a list

#And selecting multiple columns returns a DataFrame.

#even when u select a single column and use 2 brackets, it returns a dataframe...
print("\n---------------------------------------------")
print(df[["Price"]])





#-----------------------------------------------------------------------
