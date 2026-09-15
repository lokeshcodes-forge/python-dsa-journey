numbers =[1,2,3,4,1,2,3]
count ={}
for numbers in numbers:
    if numbers in count:
        count[numbers]+=1
    else:
        count[numbers]=1
print(count)
        
