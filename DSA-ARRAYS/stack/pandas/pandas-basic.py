import pandas as pd
data = {
    "name":["ram","ravi","shyam"],
    "age":[20,21,19],
    "marks":[85,92,78]


}
df = pd.DataFrame(data)
print(df)
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.head())
print(df.tail)
print(df.describe())
