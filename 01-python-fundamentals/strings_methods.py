name = "loki"
age = 20

print(f"my name is{name}and age is {age}")

name ="loki"
marks=85.5
print(f"student name is{name}marks are  {marks}")

#exx
a =10
b= 5
print(f"sum is{a+b}")
print(f"product is{a*b}")

# f  grade program
name = input("enter name")
marks =float(input("enter marks"))
if marks>=75:
    result = "distinction"
elif marks>=60:
    result = "fristclass"
else:
    result = "fail"
print(f"{name}scored {marks}and got { result}")

# anagram 
word_1= input("enter word")
word_2 =input("enter a word")
if sorted(word_1)==sorted(word_2):
    print('anagram')
else:
    print('not anagram')



word = "hello"
result= max(word,key=word.count)
print(result) 
print("hell0".isalpha)
print("hello".isdigit())
