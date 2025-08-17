import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 300)
y = np.linspace(-2, 2, 300)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

plt.imshow(Z, extent=[-2,2,-2,2], origin="lower", cmap="viridis")
plt.colorbar()
plt.show()
