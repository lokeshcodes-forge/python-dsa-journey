
#simple calculator 
def calculate(a , b, operation ):
    if operation == "add":
        return (a + b)
    elif operation == "mul":
        return ( a * b)
    elif operation == "sub":
        return ( a - b)
    elif operation ==  "div":
        return ( a / b)
    

print (calculate(10,5, "add"))
print(calculate(10,5,"mul"))
print(calculate(10,5,"sub"))
print(calculate(10,5,"div"))









    
    