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

#accesing single column: 
print("age: \n",df["Age"])


#for applying conditions on columns and getting desired values  [like SQL queries] , we have 2 ways:

#first : only one condition-

print(df[df["Age"]>25])



#second : more than one conditions-

print("\n--------------------------------")

print(df[(df["Age"] > 25) & (df["Price"] > 50000)]) #notice the syntax