import matplotlib.pyplot as plt
import numpy as np

library_name = np.array(["NumPy", "Pandas", "Matplotlib", "Scikit-learn", "TensorFlow", "Flask"])
library_rate = np.array([10, 9.5, 9, 9, 8.5, 8])

plt.title("Рейтинг найпопулярніших бібліотек Python")

plt.bar(library_name, library_rate, 0.2, color=["red", "green", "blue", "black", "magenta", "yellow"], zorder=2)

plt.xlabel('Назва бібліотеки')
plt.ylabel('Рейтинг')
plt.grid(axis='y', zorder=0)
plt.legend()
plt.show() 