import matplotlib.pyplot as plt
fig ,ax = plt.subplots(figsize=(6,4))
students = ["ram","ravi","rahul"]
marks=[85,92,78]
bars=ax.bar(students,marks,color="green")



ax.set_title("students marks")
ax.set_xlabel("students")
ax.set_ylabel("marks")
plt.ylim(50,100)
plt.xlim(0,10)
plt.yticks([0,20,40,60,80,])
plt.xticks(rotation=45)
plt.style.use("bmh")




for bar in bars :
    height =bar.get_height()
    ax.text(
        bar.get_x()+bar.get_width()/2,height,
        f"{height}",ha="center",va="bottom"
    )

plt.show()
