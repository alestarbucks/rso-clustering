import numpy as np
import random as r
import math
import matplotlib.pyplot as plt

def rso(agents, min_bound, max_bound, objective, max_steps):
    population = np.random.uniform(min_bound, max_bound, (agents, len(min_bound)))

    # print(population)
    convergence = []
    best = np.Infinity

    for rat in population:
        fitness = objective(rat)
        if fitness < best:
            best = fitness
            best_rat = rat.copy()
    convergence.append(best)
    step = 0

    C = 2 * r.random()
    R = r.random() * 4 + 1
    A = R - step * (R / max_steps)

    while step < max_steps:

        for rat_index in range(agents):
            informed_position = A * population[rat_index] + abs(C * (best_rat - population[rat_index]))
            population[rat_index] = (best_rat - informed_position)
            
            for i in range(2):
                if population[rat_index][i] < min_bound[i]:
                    population[rat_index][i] = min_bound[i]
                elif population[rat_index][i] > max_bound[i]:
                    population[rat_index][i] = max_bound[i]

        # print(population)
        
        C = 2 * r.random()
        R = r.random() * 4 + 1
        A = R - step * (R / max_steps)

        for rat in population:
            fitness = objective(rat)

            if fitness < best:
                best = fitness
                best_rat = rat.copy()

        step += 1
        convergence.append(best)
    # plt.plot(convergence)
    # plt.show()
    print(population)
    return best_rat

# objective = lambda x: x[0]**2 + x[1]**2

objective = lambda x: -(x[1] + 47) * math.sin(math.sqrt(abs(x[0] / 2 + (x[1] + 47)))) - x[0] * math.sin(math.sqrt(abs(x[0] - (x[1] + 47))))
b = rso(100, [-512, -512], [512, 512], objective, 200)
print(b)