class student :
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def show(self):
            print(f"{self.name} scored {self.marks}")

s1 = student("loki",85)                                                                 
s1.show()
s2 = student("lo",20)
s2.show()


class car:
     
     def __init__(self,brand,year):
          self.brand = brand
          self.year = year
     def show(self):
          print(f"{self.brand}bought{self.year}") 

c1 = car("def",2006)
c1.show()




        