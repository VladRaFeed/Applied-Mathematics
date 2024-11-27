import numpy as np
from scipy.stats import binom

# Задача 1: Повна ймовірність
P_A, P_B, P_C = 0.4, 0.35, 0.25  # Ймовірності автомайстерень
P_quality_A, P_quality_B, P_quality_C = 0.9, 0.8, 0.7  # Ймовірності якісного ремонту

P_qualitative_repair = (
    P_A * P_quality_A +
    P_B * P_quality_B +
    P_C * P_quality_C
)

# Метод Монте-Карло для задачі 1
np.random.seed(42)
n_simulations = 100000
workshops = np.random.choice(["A", "B", "C"], p=[P_A, P_B, P_C], size=n_simulations)
quality_probs = np.where(workshops == "A", P_quality_A,
                         np.where(workshops == "B", P_quality_B, P_quality_C))
monte_carlo_quality = np.mean(np.random.rand(n_simulations) < quality_probs)

# Задача 2: Біноміальний розподіл
n, p = 10, 0.8  # Кількість лампочок і ймовірність успіху

# Аналітичний розрахунок
P_8_lamps = binom.pmf(8, n, p)
P_at_least_7 = binom.sf(6, n, p)  # sf(6) = 1 - cdf(6)

# Метод Монте-Карло для задачі 2
lamp_trials = np.random.rand(n_simulations, n) < p  # Генеруємо успіхи для кожної лампочки
lamp_sums = lamp_trials.sum(axis=1)  # Кількість успіхів у кожному наборі
monte_carlo_8_lamps = np.mean(lamp_sums == 8)  # Рівно 8 успішних лампочок
monte_carlo_at_least_7 = np.mean(lamp_sums >= 7)  # Не менше 7 успішних лампочок

print("Задача 1: Повна ймовірність")
print(f"Аналітичний метод: {P_qualitative_repair:.3f}")
print(f"Метод Монте-Карло: {monte_carlo_quality:.3f}")

print("\nЗадача 2: Біноміальний розподіл")
print(f"Ймовірність рівно 8 лампочок (аналітично): {P_8_lamps:.3f}")
print(f"Ймовірність рівно 8 лампочок (Монте-Карло): {monte_carlo_8_lamps:.3f}")
print(f"Ймовірність не менше 7 лампочок (аналітично): {P_at_least_7:.3f}")
print(f"Ймовірність не менше 7 лампочок (Монте-Карло): {monte_carlo_at_least_7:.3f}")
