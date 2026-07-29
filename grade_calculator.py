math = int(input("enter a num"))
sci  = int(input("enter anum"))
soc  = int(input("enter anum"))
phy =  int(input("enter a num"))

avg = (math+sci+soc+phy)/4

if(avg>=90):
    print("a grade")
elif(avg>=70):
    print("b grade")
elif(avg>=60):
    print("c grade")
else:
    print("fail")        
    # grade calculator
