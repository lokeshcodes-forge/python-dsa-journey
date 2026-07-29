class employee:
    def __init__(self,name):
        self.name=name
    def bonous(self):
        print(f"{self.name}bonous is 9")    
        
class manager(employee):
    def __init__(self, name):
        self.name=name
    def bonous(self):
        print(f"{self.name}bonous is 7")

class intern(employee):
    pass

m1=manager("loki")
m1.bonous()

i1 =intern("sai")
i1.bonous()

