import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Shyam", "Kiran"],
    "Date": ["2025-01-15", "2024-12-20", "2023-06-10", "2022-09-05"]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("----------------")

df["Date"] = pd.to_datetime(df["Date"])

print("Date Format")
print(df)

print("----------------")

print("Year")
print(df["Date"].dt.year)

print("----------------")

print("Month")
print(df["Date"].dt.month)

print("----------------")

print("Day")
print(df["Date"].dt.day)
