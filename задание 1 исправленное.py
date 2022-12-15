import matplotlib.pyplot as plt
import numpy as np
import os

if not os.path.isdir("results"):
    os.mkdir("results")

A = 512
x = np.linspace(-512, 512, 1000)
y = -(A+47)*np.sin(np.sqrt(abs(x/2+(A+47))))-x*np.sin(np.sqrt(abs(x-(A+47))))
plt.axis([-512, 512, -1500, 1500])
plt.plot(x, y)
plt.show()

with open(r'results\results.txt', "w", encoding="utf-8") as file:
    file.write("x    y\n")
    for i in range(len(x)):
        file.write("{}    {}\n".format(x[i], y[i]))
