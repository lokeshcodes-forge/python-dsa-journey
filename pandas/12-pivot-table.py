import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Shyam", "Kiran", "Mohan"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Marks": [85, 92, 78, 95, 88]
}

df = pd.DataFrame(data)

print(df)

print("----------------")

pivot = df.pivot_table(
    values="Marks",
    index="City",
    aggfunc="mean"
)

print(pivot)