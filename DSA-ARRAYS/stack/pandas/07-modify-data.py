import pandas as pd
data ={
    "name":["ram","ravi","shyam","loki"],
    "age":[20,21,12,22],
    "marks":[85,12,78,95]

    
}

df=pd.DataFrame(data)

df["city"]=["delhi","mumbai","hyderabad","atp"]
df.loc[2,"age"]=25
df.loc[1,"name"]="lokii"
df.loc[1,"city"]="atp"
df.rename(columns={"marks":"score"})


print(df)












