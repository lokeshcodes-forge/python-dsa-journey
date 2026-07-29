# internet speed 
speed = float(input ("enter mbps :"))
if speed >= 100 :
    print("excellent")
elif speed >=50 :
    print("good")
elif speed>=20:
    print("avg")
else:
    print("poor connection")

# atm 
card = input("enter the num:")
pin = input("enter pin:")
amount = int(input("enter amount:"))

if card == "1234"and pin == "9999":
    if amount <= 10000  :
        print("dispensing amount")
    else:
        print("limit excedss")
else:
    print("invalid")
# job apllication 
age = int(input("enter age :"))
exp = int(input("enter exp :"))
if age >= 18 and exp >=2:
    print("application accepted")
elif age>=18 and exp< 2:
    print("more exp")
elif age<18:
    print(" too young ")
else:
    print("no age limit")




