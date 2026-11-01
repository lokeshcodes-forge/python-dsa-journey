import pandas as pd
data = {
    "name":["ram","ravi","shyam"],
    "age":[20,21,19],
    "marks":[85,92,78]

}
df =pd.DataFrame(data)
print(df)
print(df["age"])
print(type(df["age"]))
print(type(df[["name","marks"]]))
# iloc stands for integer location
print(df.iloc[0])
print(df.iloc[1])
print(df.iloc[2])
print(df.iloc[1,2])
print(df.iloc[2,1])
print(df.iloc[0:2])
#loc means rowlabel and colname.

print(df.loc[1])
print(df.loc[1,"age"])
print(df.loc[0,"marks"])
print(df.loc[2,"name"])






