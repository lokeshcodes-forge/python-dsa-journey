contacts = {
    "rahul": 7013780231,
    "loki": 900466985,
    "priya":9949279319

}

print(contacts["rahul"])
print(contacts["priya"])

student= {
    "name":"loki",
    "age":20,
    "marks":85

}
print(student["name"])
print(student["age"])

student = {"name":"loki","age":20,}

student["marks"]=85
print(student)
student["age"]=21
print(student)
del student["age"]
print(student)

car = {"brand":"landrover","model":"defender","year":2020}

car["year"] = 2024
del car["model"]
print(car)

bike = {"brand":"honda","model":"2021","year":"2001","price":"2"}

print(bike["brand"])
print(bike["model"])
print(bike["price"])


person ={"name":"loki","age":"20","city":"atp","clg":"nnnaaaa"}
print(person["name"],
      person["age"],
      person["city"],
      person["clg"])

person ={"name":"loki","age":"20","city":"atp","clg":"nnnaaaa"}
for key in person:
    print(key,":",person[key])

prices={"apple":50,"mango":80,"banana":20,"grapes":120}
for key in prices:
    if prices [key]<=70:
        print(key,":",prices[key])


scores={"loki":85,"rahul":92,"priya":78,"sam":95}
print(max(scores.values()))
print(len(scores))
print(scores.keys())


students ={"lo":80,"so":90,"mo":20,"no":10}
for key in students:
    print(key,":",students[key])

print("highest:",max(students.values()))
print("lowest:",min(students.values()))

for key in students:
    if students[key]>80:
        print(key)

students = {
    "loki":{"age":20,"marks":85},
    "rahul":{"age":21,"marks":90},

}
print(students["loki"]["marks"])
print(students["rahul"]["marks"])

student = {"name":"loki","age" :21}

if "name" in student:
    print("key exisit")
if "marks"in student:
   print("has marks")
else:
    print("no marks key")


squares = { x: x*x for x in range(1,6)}
print(squares)

# tuples and sets



fruits = {"aa","bb","cc","dd","OO"}
fruits.add("ll")
fruits.remove("aa")
print(fruits)
print(len(fruits))

a = {1,2,3}
b ={2,3,4}
print(a|b)
print(a & b)
print(a - b)






