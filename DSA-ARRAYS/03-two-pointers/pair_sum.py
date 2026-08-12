numbers=[1,2,4,6,8,10]
target=10
left =0
right=len(numbers)-1
while left<right:
      sum= numbers[left]+numbers[right]
      if sum == target:
            print(numbers[left],numbers[right])
            break
      elif sum<target:
            left+=1
      else:
            right-=1  


   #partice question02
numbers=[1,2,4,5,6,7,8]
target=15
left=0
right=len(numbers)-1
while left<right:
      sum = (numbers[left]+numbers[right])
      if sum==target:
            print(numbers[left],numbers[right])
            break
      elif sum<target:
            left+=1
      else:
            right-=1
            
            

   

                      
            

