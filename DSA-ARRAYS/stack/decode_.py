s = "3[a]2[bc]"

stack = []
current = ""

for ch in s:
    if ch == "[":
        stack.append(current)
        current = ""

    elif ch == "]":
        previous = stack.pop()
        current = previous + current

    else:
        current += ch

print(current)