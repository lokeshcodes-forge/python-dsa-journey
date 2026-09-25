nums = [7,2,4,8,5,2,3]
stack =[]
answer= [-1]*len(nums)
for i in range(len(nums)):
    current = nums[i]
    while stack and stack[-1]>=current:
        stack.pop()
    if stack:
        answer[i]=stack[-1]
    stack.append(current) 
print(answer)           

