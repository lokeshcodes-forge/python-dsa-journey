class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
        
    def area(self):
        return self.length*self.width   

class triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):    
        return 0.5*self.base*self.height


s1 = rectangle(2,10)
s2=triangle(12,2)  


shapes = [ s1,s2]
for shape in shapes:
    print(shape.area())