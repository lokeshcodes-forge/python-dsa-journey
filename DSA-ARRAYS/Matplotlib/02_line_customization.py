import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(
    x,
    y,
    color="blue",
    linewidth=3,
    linestyle="--",
    marker="o",
    label="Sales"
)

plt.title("Monthly Sales")

plt.xlabel("Month")

plt.ylabel("Sales")

plt.grid(True)

plt.legend()

plt.show()



months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [20, 35, 30, 45, 50]

plt.plot(
    months,
    sales,
    color="red",
    linewidth=3,
    linestyle="--",
    marker="o",
    label="Sales"
)

plt.title("Monthly Sales")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.grid(True)
plt.legend()

plt.show()