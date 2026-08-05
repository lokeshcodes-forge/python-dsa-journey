class person:
    def __init__(self,name):
        self.name=name

class student(person):
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
        super().__init__(name)
        print(f"{self.name}and{self.grade}")
class teacher(person):
    pass

s1 = student("loki","a")

t1= teacher("sai")
print(t1.name)
