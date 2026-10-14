import pandas as pd
df =pd.read_csv("DSA-ARRAYS/stack/pandas/students.csv")
print(df)
df.to_csv ("new_students.csv",index=False)
print("new csv file created succesfully.")

