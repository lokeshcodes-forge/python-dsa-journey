# grade converter
def grade (marks):
    if marks >= 75:
        result = "distinction"
    elif marks >=60:
        result = " frist class"
    else:
        result = "fail"
    return result 

marks = float(input("enter marks :"))
result = grade (marks)
print(result)
    


    # login system

def login (username , password) :
    if username == "admin" and password == "1234" :
        result = "login success"
    elif username == "admin" :
        result = " wrong " 
    else:
        result = "userno" 
    return result    

username = input("enter username:")
password = input(" enter password")
result = login(username,password)
print(result)



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

# even odd

def iseven (num):
    if num%2==0:
        return"even"
    else:
        return"odd"
    
n = int(input("enter anum"))
result = iseven(n)
print(result)








    
    