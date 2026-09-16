nums = [6,1,4,8,3]
stack = []
answer = [-1]*len(nums)
for i in range (len(nums)-1,-1,-1):
    current=nums[i]

    while stack and stack[-1]<=current:
        stack.pop()
    if stack:
        answer[i]=stack[-1]
    stack.append(current)

print(answer)
        