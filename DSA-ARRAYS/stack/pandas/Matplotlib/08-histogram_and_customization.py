import matplotlib.pyplot as plt

marks= [52,62,42,8,42,95,85,6,85,6,85,85,85,8,5,78]
plt.hist(marks,
         bins=5,
         color="green",
         edgecolor="blue",
         alpha=0.2)
plt.title("marks frequency")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()
