temp = [74,85,98,25,82,91]
answer=[0]*len(temp)
stack=[]
for i in range (len(temp)-1,-1,-1):
    current = temp[i]
    while stack and temp [stack[-1]]<=current:
        stack.pop()
    if stack:
        answer[i]=stack[-1]-i
    
    stack.append(i)
print(answer)            