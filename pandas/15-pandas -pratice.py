import pandas as pd

data = {
    "Name": ["Ram", "Ravi", "Shyam", "Kiran", "Ram"],
    "City": ["Delhi", "Mumbai", "Delhi", "Mumbai", "Delhi"],
    "Marks": [85, 92, None, 95, 85],
    "Age": [20, 21, 19, 22, 20]
}

df = pd.DataFrame(data)

print("Original Data")
print(df)

print("----------------")

print("Head")
print(df.head())

print("----------------")

print("Info")
print(df.info())

print("----------------")

print("Describe")
print(df.describe())

print("----------------")

print("Students with Marks > 80")
print(df[df["Marks"] > 80])

print("----------------")

print("Sort by Marks")
print(df.sort_values(by="Marks", ascending=False))

print("----------------")

print("Fill Missing Values")
df["Marks"].fillna(0, inplace=True)
print(df)

print("----------------")

print("Add New Column")
df["Result"] = ["Pass", "Pass", "Fail", "Pass", "Pass"]
print(df)

print("----------------")

print("Modify One Value")
df.loc[2, "Marks"] = 75
print(df)

print("----------------")

print("Rename Column")
df = df.rename(columns={"Marks": "Score"})
print(df)

print("----------------")

print("Group By City")
print(df.groupby("City")["Score"].mean())

print("----------------")

print("Pivot Table")
print(df.pivot_table(values="Score", index="City", aggfunc="mean"))

print("----------------")

print("Unique Cities")
print(df["City"].unique())

print("----------------")

print("Value Counts")
print(df["City"].value_counts())

print("----------------")

print("Remove Duplicates")
print(df.drop_duplicates())

print("----------------")

print("Upper Case Names")
print(df["Name"].str.upper())

print("----------------")

df["Date"] = pd.to_datetime([
    "2025-01-10",
    "2025-02-15",
    "2025-03-20",
    "2025-04-25",
    "2025-05-30"
])

print("Year")
print(df["Date"].dt.year)

print("----------------")

print("Final Data")
print(df)