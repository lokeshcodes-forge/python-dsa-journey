
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











    
    