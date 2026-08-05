customername = input("enter name:")
billamount = int(input("enter bill amount:"))

if billamount >= 5000:
    discount = 20
elif billamount >= 3000:
    discount = 15
elif billamount >= 1000:
    discount = 10
else:
    discount = 0

discount_amount = billamount * discount / 100
final = billamount - discount_amount

print("Hello " + customername)
print("Your bill is: " + str(billamount))
print("Discount: " + str(discount) + "%")
print("Final amount: " + str(final))










