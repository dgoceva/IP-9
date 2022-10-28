import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()
ax.set_xlabel('X')
ax.set_ylabel('SIN(x)')
points = ax.plot(x, y)
plt.setp(points, color='green', linestyle='dashdot', linewidth=3)
plt.show()
