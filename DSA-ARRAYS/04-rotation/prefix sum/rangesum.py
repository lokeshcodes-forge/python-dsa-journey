numbers=[3,7,2,5,8,4]
left = 2
right = 5
prefix =[0]*len(numbers)
prefix[0]=numbers[0]
for i in range(1,len(numbers)):

    prefix[i] = prefix[i-1] + numbers[i]
    prefixsum=prefix[right] - prefix[left-1]
print(prefixsum)    
