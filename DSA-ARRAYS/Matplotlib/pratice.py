import matplotlib.pyplot as plt

students = ["Ram", "Ravi", "Rahul", "Sai"]
marks = [80, 92, 75, 88]

plt.figure(figsize=(12,8))

# 1. Bar Chart
plt.subplot(2,2,1)
plt.bar(students, marks, color="skyblue")
plt.title("Bar Chart")

# 2. Pie Chart
plt.subplot(2,2,2)
plt.pie(marks, labels=students, autopct="%1.1f%%")
plt.title("Pie Chart")

# 3. Line Plot
plt.subplot(2,2,3)
plt.plot(students, marks, marker="o", color="green")
plt.title("Line Plot")

# 4. Scatter Plot
plt.subplot(2,2,4)
plt.scatter(students, marks, color="red", s=100)
plt.title("Scatter Plot")

plt.tight_layout()

plt.show()