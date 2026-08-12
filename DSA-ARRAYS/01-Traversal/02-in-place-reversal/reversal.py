numbers = [15,25,35,45,55,65]
left=0
right=len(numbers)-1
while left<right:
    numbers[left],numbers[right] =    numbers[right],numbers[left]
    left+=1
    right-=1
print(numbers)



    # partice question 2
numbers =[10,20,30,40,50,60]
left =0
right=len(numbers)-1
while left<right:
    numbers[left],numbers[right]= numbers[right],numbers[left]
    left+=1
    right-=1
print(numbers)    



