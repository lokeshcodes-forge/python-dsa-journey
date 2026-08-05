class wallet:
    def __init__(self):
        self.balance=0
    def addmoney(self,amount):
        if amount>0:
            self.balance+=amount
        else:
            print("invalid")

    def getbalance(self):
        return self.balance



w1 = wallet()
w1.addmoney(-100)
w1.addmoney(500)
print(w1.getbalance())    