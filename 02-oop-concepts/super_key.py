class employee:
    def __init__(self,name):
        self.name =name
    def bonous(self):
        print(f"{self.name}bonous is 11")

        
class manager(employee):
    def __init__(self, name):
        self.name=name
    def bonous(self):
        super().bonous()
        print("extrabonous is 12")

m1 = manager("loki")
m1.bonous()                    