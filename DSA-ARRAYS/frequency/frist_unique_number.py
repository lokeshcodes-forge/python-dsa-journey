numbers =[3,5,3,8,5,9,8]
count={}
for number in numbers:
    if number in count:
        count[number]+=1
    else:
        count[number]=1
for number in numbers :
    if count[number]==1:
        print(number)
        break        