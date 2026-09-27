prices =[100,20,30,85,97]
stack = []

for price in prices:
    span =1
    while stack and stack[-1][0]<=price:
        span+=stack.pop()[1]
    stack.append((price,span))
print(stack)        