s = " erase*****"
stack=[]
for ch in s :
    if ch =="*":
        stack.pop()
    else:
        stack.append(ch)
print("".join(stack))


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
      
      
  def pop(self,val):
    self.pop .ministack(val)
    self.pop .minimumstack(val)
  def top (self):
    return self.ministack [-1]
    
    
  def getmin(self):
    return self.ministack[-1]
    



minimumstack = [5,3,3]
val = 4 

    
    
    
  
