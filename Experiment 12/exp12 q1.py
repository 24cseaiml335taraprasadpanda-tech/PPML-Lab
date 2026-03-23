import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,40]
plt.plot(x,y)
plt.title("Simple line plot")
plt.plot(x,y,linestyle="__",color="r",marker=0,label="Data line")
plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")
plt.legend()
plt.grid()
plt.show()