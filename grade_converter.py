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









    
    