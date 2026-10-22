import pandas as pd

data = {
    "Name": ["  ram", "RAVI", "Shyam ", "kiRan", "mohan"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("----------------")

print("Upper")
print(df["Name"].str.upper())

print("----------------")

print("Lower")
print(df["Name"].str.lower())

print("----------------")

print("Title")
print(df["Name"].str.title())

print("----------------")

print("Contains 'am'")
print(df["Name"].str.contains("am"))

print("----------------")

print("Replace")
print(df["Name"].str.replace("ram", "Rahul"))

print("----------------")

print("Remove Spaces")
print(df["Name"].str.strip())