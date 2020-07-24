import matplotlib.pyplot as plt

x = [1,2,3]
y = [6,7,8]

z = [1,2,3]
w = [6,7,8]

plt.title("Deaths by mms")
plt.xlabel("axis x")
plt.ylabel("axis y")
plt.plot(x,y)
plt.bar(x,y)
plt.bar(x,y, label="orange bars")
plt.bar(z,w, label="blue bars")
plt.show()
