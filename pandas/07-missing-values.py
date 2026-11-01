import pandas as pd
data ={
    "name":["ram","ravi","shyam","kiran"],
    "age":[20,21,None,22],
    "marks":[85,None,78,95]

    
}
df=pd.DataFrame(data)
print(df)
print(df.isnull())
print(df.notnull())
print(df.dropna())
print(df.fillna(1403))
print(df.fillna(1403,inplace=True))










