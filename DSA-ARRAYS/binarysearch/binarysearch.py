numbers = [2,6,9,14,18,23,27,31,40]
target = 31


left = 0
right = len(numbers)-1

while left<= right:
    middle=(left+right)//2
    if numbers[middle]==target:
        print("found")
        found = True
        break
    elif target>numbers[middle]:
        left=middle+1
    else:
        right=middle-1
        
    print("notfound")
    found = False



