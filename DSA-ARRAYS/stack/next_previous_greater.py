nums = [8,1,1,25,9]
answer = [-1]*(len(nums))
stack = []
for i in range(len(nums)):
    current = nums[i]
    while stack and stack[-1]<= current:
        stack.pop()
    if stack:
        answer[i]=stack[-1]
    stack.append(current)
print(answer)        