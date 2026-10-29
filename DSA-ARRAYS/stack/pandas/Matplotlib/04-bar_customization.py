import matplotlib.pyplot as plt 
students =["loki","sai","mash","bhushan","mmmm"]
marks=[85.52,96,74,85,99]
plt.bar(
    students,marks,color ="red",edgecolor = "black",width=1,label=marks

)
plt.title("shanmukh^s data")
plt.xlabel("students names")
plt.ylabel("studentmarks")
plt.grid(axis="y")
plt.legend()
plt.show()
