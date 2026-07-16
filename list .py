marks=[85,90,78]
print("original:",marks)
marks.append(92)
print("after append:",marks)
marks.remove(90)
print("after sort :",marks)
marks.reverse()
print("after reverse:",marks)


marks = [85,90,78,92]
print(len(marks))
marks.append(95)
print(len(marks))
marks =[85,90,78,92,88]
total = 0
for mark in marks:
    total = total + mark
avg = total / len(marks)

print("total :",total)
print ("avg :",avg)



marks = [85,90,78,92,88]
print(marks[0:3])
print(marks[-3:])
print(marks[2])



# avg function
def avg(marks):
    total= 0
    for mark in marks :
        total = total + mark
    return total/ len(marks)
    
marks = [90,80,20,11]
result = avg(marks)
print("avg:",result)

# hihest and lowest fun inlist
def find_highest(number):
    return max(number)

numbers = [10,20,30,100]
result = find_highest(numbers)
print("highest number:",result)


def find_lowest(number):
    return min(number)

numbers = [10,203,0,302020]
result = find_lowest(numbers)
print("lowest number :",result)

   #list compp
squares = [i*i for i in range(1,6)]
print(squares)

numbers = [x for x in range(1,6)]
print(numbers)

numbers = [ x for x in range (1,11)if x%2!=0]
print(numbers)

numbers = [ x * 2 for x in range(1,6)]
print(numbers)

big = [ x for x in[85,52,852,8520]if x>85]
print(big)
    