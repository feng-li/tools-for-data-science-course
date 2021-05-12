import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np


def calculator(mu, k):
    """mu: rate * t"""
    return mu ** k / np.math.factorial(k) * np.exp(-mu)


x = np.linspace(1, 30, 30)
z = np.array([[calculator(i, j) for i in x] for j in x])
x, y = np.meshgrid(x, x)


fig = plt.figure()
ax = fig.gca(projection = '3d')
ax.set_xlabel('mu')
ax.set_ylabel('k')
ax.set_zlabel('P')
ax.plot_surface(x, y, z, cmap=cm.gray)
plt.show()