class bankaccount:
    def __init__(self,balance):
        
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("amount added")
        else:
            raise ValueError("insufficent funds")

    def withdraw(self,amount):
        if amount<self.__balance:
            self.__balance-=amount
            print("money withdrawn")
        else:
            raise ValueError("failed to withdrawn")

    def getbalance(self):
        return self.__balance



b1 = bankaccount(100)
b1.deposit(20)
b1.withdraw(100)

print(b1.getbalance())

