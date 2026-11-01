import matplotlib .pyplot as plt
subjects = ["py","pd","np","plt"]
hours=[90,85,12,96]
plt.pie(hours,labels=subjects)
plt.title("study time")
plt.show()
