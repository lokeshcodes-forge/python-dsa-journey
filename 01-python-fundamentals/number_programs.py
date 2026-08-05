# reverse 
num = int(input("enter anumber:"))
reverse = 0
while num> 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse)

# sum
num = int (input("enter a number :"))
total = 0
while num >0:
    digit = num % 10
    total = total + digit
    num = num // 10
print(total)   

#count
num  = int(input("enter a number"))
count = 0
while num >0:
    count = count+1
    num = num //10
print(count)
# palndrome

num = int(input("enter a number "))
orignal = num
reverse = 0
while num>0:
    reverse = reverse *10 + num 
    if orignal == reverse:
        print("palindrome")
    else:
        print("not")



