numbers = [10,20,30,40,50,60,70]
k =3
k = k%len(numbers)
left=0
right=len(numbers)-1
while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left+=1
    right-=1


left=0
right=k-1

while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left +=1
    right-=1


left=k
right=len(numbers)-1

while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left+=1
    right-=1

print(numbers)    










# 02
numbers =[1,2,3,4,5,6,7,8]
k=3
k=k%len(numbers)
left=0
right=len(numbers)-1
while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left+=1
    right-=1

left =0
right=k-1

while left<right:
    numbers[left],numbers[right]=numbers[right],numbers[left]
    left+=1
    right-=1


left = k
right=len(numbers)-1

while left<right:
        numbers[left],numbers[right]=numbers[right],numbers[left]
        left+=1
        right-=1
print(numbers)
        

     


