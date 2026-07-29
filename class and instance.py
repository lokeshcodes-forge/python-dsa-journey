class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


s1=student("loki",95)
s2=student("lo",85)
s3=student("sai",80)


s2.marks=95
s2.marks=100


print(s1.name,s1.marks)
print(s2.name,s2.marks)
print(s3.name,s3.marks)


class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author

b1=book("aromic habits","jamesclear")
b2 = book("wings of fire","apj")

print(b1.title,b1.author)
print(b2.title,b2.author)

class car:
    def __init__(self,brand):
        self.brand=brand

c1= car("r")
c2= car("land")
c3=car("ol")


print(c1.brand)
print(c2.brand)
print(c3.brand)

class phone:
    def __init__(self,brand,price):
        self.price=price
        self.brand=brand
p1=phone("vivo" ,10000)
p2= phone("oppo",20000)


print(f"{p1.brand}ost{p1.price}")
print(f"{p2.brand}ola{p2.price}")





