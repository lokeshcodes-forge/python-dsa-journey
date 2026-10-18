import pandas as pd
students ={
    "id":[1,2,3],
    "name":["loki","mash","kanta"]

}

marks= {
    "id":[1,2,3],
    "marks":[85,92,78]


}




df1= pd.DataFrame(students)
df2=pd.DataFrame(marks)
print(df1)
print(df2)
result=pd.merge(df1,df2,on="id",how="right")
result=pd.merge(df1,df2,on="id",how="left")
result=pd.merge(df1,df2,on="id",how="inner")
result=pd.merge(df1,df2,on="id",how="outer")



print(result)
