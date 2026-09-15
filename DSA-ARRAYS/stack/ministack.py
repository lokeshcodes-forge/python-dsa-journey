class ministack:
  def __init__(self):
    self.ministack =[]
    self.minimumstack=[]
  def push(self,val):  
    self.ministack .append(val)
    if not self.minimumstack:
      self.minimumstack. append(val)
    else:
      newminimum = min(val,self.minimumstack[-1])
      self.minimumstack.append(newminimum)
      
      
  def pop(self,):
    self.ministack.pop()
    self.minimumstack.pop()
  def top (self):
    return self.ministack [-1]
    
    
  def getmin(self):
    return self.ministack[-1]
    

s = ministack()
s.push(5)
s.push(3)
s.push(7)
s.push(2)
print(s.minimumstack)
print(s.ministack)

s.pop()

print(s.ministack)
print(s.minimumstack)


    
    
    
  