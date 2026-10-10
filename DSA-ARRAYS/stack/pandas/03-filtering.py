import pandas as pd
data ={
    "name":["ram","ravi","shyam","kiran"],
    "age":[20,21,19,22],
    "marks":[85,92,78,95]

    
}
df=pd.DataFrame(data)
print(df)
print(df[df["marks"]>80])
print(df[df["age"]<20])
print(df[df["name"]=="ram"])
print(df[df["marks"]>=85])
print(df[df["name"]!="ram"])
