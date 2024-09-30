import matplotlib.pyplot as plt
import numpy as np

labels = ["Архітектура комп'ютера", "ООП", "АСД", "КГВ", "ООКП", "ЙОПІ"]
values1 = [85, 90, 88, 83, 85, 92]
values2 = [83, 80, 81, 86, 90, 88]

width = 0.2

i = np.arange(6)

plt.bar(i - width/2, values1, width, label='ІПЗ-24', color="blue", zorder=2)
plt.bar(i + width/2, values2, width, label='ІПЗ-25', color="Yellow", zorder=2)

plt.xlabel('Предмет')
plt.ylabel('Середній бал')
plt.title('Угрупована діаграма показників оцінок учнів з двох груп')
plt.xticks(i, labels)
plt.grid(axis='y', zorder=0)
plt.legend()

plt.show()