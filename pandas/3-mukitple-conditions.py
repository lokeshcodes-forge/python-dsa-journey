import pandas as pd
data ={
    "name":["ram","ravi","shyam","kiran"],
    "age":[20,21,19,22],
    "marks":[85,92,78,95]

    
}
df=pd.DataFrame(data)
print(df)
print(df[(df["Marks"] > 80) & (df["Age"] < 20)])



