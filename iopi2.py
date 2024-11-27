import random

def monte_carlo_simulation_fixed(num_employees, num_simulations, work_minutes=480):
    at_least_two = 0
    at_least_three = 0

    for _ in range(num_simulations):
        arrivals = [random.randint(1, work_minutes) for _ in range(num_employees)]
        unique_arrivals = set(arrivals)
        
        # Count how many employees arrive at the same minute
        counts = [arrivals.count(minute) for minute in unique_arrivals]
        
        if max(counts) >= 3:
            at_least_three += 1  # If three arrive, two also arrive
            at_least_two += 1
        elif max(counts) >= 2:
            at_least_two += 1

    prob_two = at_least_two / num_simulations
    prob_three = at_least_three / num_simulations

    return prob_two, prob_three

# Parameters
num_employees = 10
num_simulations = 100000

# Run simulation
probability_two, probability_three = monte_carlo_simulation_fixed(num_employees, num_simulations)

print(f"{probability_two:.5f}")
print(f"
      {probability_three:.5f}")
