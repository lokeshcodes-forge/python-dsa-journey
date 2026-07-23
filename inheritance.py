#class parent
class vehicle:
    def __init__(self,brand):
        self.brand=brand

    def start(self):
            print(f"{self.brand}is starting")

#class child
class bike(vehicle):
    pass
class truck(vehicle):
    def load_cargo(self):    
        print("cargoloaded")

b1=bike("rx")
b1.start()

t1=truck("volvo")
t1.start()
t1.load_cargo()        
