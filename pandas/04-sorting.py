import pandas as pd
data = {
    "name":["ram","ravi","shyam"],
    "age":[20,21,19],
    "marks":[85,92,78]

}
df =pd.DataFrame(data)
print(df)

print(df.sort_values("marks"))

print(df.sort_values("marks", ascending=False))

print(df.sort_values("age"))

print(df.sort_values("name"))

print(df.sort_values(["marks", "age"]))

df.sort_values("marks", inplace=True)
print(df)