import matplotlib.pyplot as plt
sub =["py","pd","np","plt"]
hours=[40,85,56,12]
colors=["skyblue","red","green","black"]
explode=[0.1,0,0,0]
plt.pie(hours,labels=sub,colors=colors,
        autopct="%1.1f%%",shadow=True,startangle=90)
plt.title("study time")
plt.show()