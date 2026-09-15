numbers = [3,7,2,5]
prefix =[0]*len(numbers)
prefix[0] = numbers[0]
for i in range(1, len(numbers)):
    prefix[i] = prefix[i-1] + numbers[i]
print(prefix)    