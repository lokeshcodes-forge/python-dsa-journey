import pandas as pd
data ={
    "name": ["ram","ravi","shyam","kiran","mohan"],
    "city":["delhi","mumbai","delhi","atp","ptp"],
    "marks":[85,92,78,95,88]

}
df = pd.DataFrame(data)
print(df)
print(df.groupby("city").sum())
print(df.groupby("city").mean(numeric_only=True))
print(df.groupby("city").count())
print(df.groupby("city").min())
print(df.groupby("city").max())





