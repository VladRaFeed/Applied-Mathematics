import matplotlib.pyplot as plt
import numpy as np

labels = ["NumPy", "Pandas", "Matplotlib", "Scikit-learn", "TensorFlow", "Keras"]
values = [26.53, 20.41, 16.33, 14.29, 12.24, 10.20]
explode = [0,0.2,0.2,0,0,0]
colors = ["tomato", "magenta", "yellowgreen", "lime", "gray", "pink"]

plt.pie(values, labels=labels, colors=colors, explode=explode, shadow=True, autopct='%.2f%%')

plt.title('Використання найпопулярніших бібліотек Python')
plt.grid()
plt.tight_layout()

plt.show()