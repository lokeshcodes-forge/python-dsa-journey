class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def raise_salary(self,percent):
        self.salary+=self.salary*percent/100
        print(f"{self.name}bonous added to ,{self.salary}")

class manager(employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.salary+=5000
    def raise_salary(self, percent):
        return super().raise_salary(percent)    
        print(f"{self.name}extra bonous is addedto,{self.salary}")


m1=manager("sai",2000)
m1.raise_salary(20)                