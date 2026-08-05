
name = input("enter your name:")
sub1 = int(input("enter marks:"))
sub2 = int(input("enter  marks:"))
sub3 = int(input("enter marks"))

avg = (sub1 + sub2 + sub3) / 3

if avg >= 75:
    result = "distinction "
elif avg >= 60:
    result = "frist class"
elif avg >= 50:
    result = "second class"
else:
    result = "fail"
print(name + " got " + result)





