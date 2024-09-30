import matplotlib.pyplot as plt
import numpy as np

random_integers1 = np.random.randint(0, 100, size=10)
random_integers2 = np.random.randint(0, 100, size=10)
random_colors = np.random.randint(0, 100, size=10)

plt.scatter(random_integers1, random_integers2, c=random_colors, marker='^')

plt.title('Діаграма розкидних даних')
plt.grid()
plt.tight_layout()

plt.show()