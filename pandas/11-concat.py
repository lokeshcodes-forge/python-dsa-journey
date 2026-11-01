import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Ram", "Ravi"]
})

df2 = pd.DataFrame({
    "Marks": [85, 92]
})

result = pd.concat([df1, df2], axis=1)

print(result)