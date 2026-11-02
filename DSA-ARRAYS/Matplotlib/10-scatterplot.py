import matplotlib.pyplot as plt

hours = [1, 2, 3, 4, 5]
marks = [40, 50, 60, 75, 90]

plt.scatter(hours, marks,color="green",marker="x",s=200
            
            )

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.savefig("scatterplot.png")
plt.grid("True")
plt.legend()
plt.figure(figsize=(20,10))


plt.show()