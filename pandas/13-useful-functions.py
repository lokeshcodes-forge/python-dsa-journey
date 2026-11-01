import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Hyderabad", "Mumbai"],
    "Name": ["Ram", "Ravi", "Ram", "Shyam", "Ravi"]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)



print("Unique Cities")
print(df["City"].unique())


print("Number of Unique Cities")
print(df["City"].nunique())



print("Value Counts")
print(df["City"].value_counts())



print("Duplicate Rows")
print(df.duplicated())



print("After Removing Duplicates")
print(df.drop_duplicates())



print("Random 1 Row")
print(df.sample())



print("Random 2 Rows")
print(df.sample(2))
import pandas as pd

data = {
    "City": ["Delhi", "Mumbai", "Delhi", "Hyderabad", "Mumbai"],
    "Name": ["Ram", "Ravi", "Ram", "Shyam", "Ravi"]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

print

print("Unique Cities")
print(df["City"].unique())



print("Number of Unique Cities")
print(df["City"].nunique())


print("Value Counts")
print(df["City"].value_counts())



print("Duplicate Rows")
print(df.duplicated())



print("After Removing Duplicates")
print(df.drop_duplicates())



print("Random 1 Row")
print(df.sample())


print("Random 2 Rows")
print(df.sample(2))