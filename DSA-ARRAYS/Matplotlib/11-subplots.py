import matplotlib.pyplot as plt
students = ["rahul","ravi","ram"]
marks = [90,75,85]
plt.subplot(1,2,1)
plt.bar(students,marks)
plt.title("bargraph")
plt.subplot(2,2,1)
plt.pie(marks,labels=students,autopct="%1.1f%%")
plt.title("piechart")
plt.tight_layout()

plt.show()
