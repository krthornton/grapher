import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

# Compute pie slices
N = 20
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = 10 * 1
width = np.pi / 4 * 1

ax = plt.subplot(111, projection='polar')
bars = ax.bar(theta, radii, width=width, bottom=0.0)

for bar in bars:
    bar.set_facecolor((0.153894, 0.680203, 0.504172, 1.0))
    bar.set_alpha(0.5)

plt.show()
