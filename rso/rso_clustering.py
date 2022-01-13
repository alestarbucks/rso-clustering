import numpy as np
import random as r
# import matplotlib.pyplot as plt

import pandas as pd
import tqdm
# import numpy as np
# import sklearn.cluster as cluster
# from rso import rso_clustering

def addc(rat, rat_index, distance, cluster_assignments, n):
    """ADDC: Average Distance to Cluster Centroid"""

    cluster_index = 0
    fitness = 0

    for cluster in cluster_assignments[rat_index]:
        if len(cluster) == 0: continue

        aux = 0

        for instance in cluster:
            aux += distance(rat[cluster_index], instance)
        
        fitness += aux/len(cluster)
    
    return fitness/len(rat)

def rso_clustering(instances, agents, k, min_bound, max_bound, distance, max_steps):
    population = []
    n = instances.shape[0]
    # corr = 0

    convergence = []
    best = np.Infinity
    cluster_assignments = [[[] for _ in range(k)] for _ in range(agents)]
    
    for i in range(agents):
        population.append(np.array(r.sample(list(instances), k)))

    rat_index = 0
    for rat in population:
        for instance in instances:
            distances = [distance(instance, rat[i]) for i in range(k)]
            cluster = np.argmin(distances)
            cluster_assignments[rat_index][cluster].append(instance)

        fitness = addc(rat, rat_index, distance, cluster_assignments, n)
        if fitness < best:
            best = fitness
            best_rat = rat.copy()
        rat_index += 1
    
    convergence.append(best)

    step = 0

    C = 2 * r.random()
    R = r.random() * 4 + 1
    A = R - step * (R / max_steps)

    for step in tqdm.tqdm(range(max_steps)):
        for rat_index in range(agents):
            # print(A, population[rat_index], C, best_rat)
            # print(len(population[rat_index]))
            informed_position = A * population[rat_index] + abs(C * (best_rat - population[rat_index]))
            population[rat_index] = (best_rat - informed_position)
            
            for centroid in range(k):
                for coord in range(min_bound.shape[0]):
                    if population[rat_index][centroid][coord] < min_bound[centroid][coord]:
                        # corr += 1
                        # print("Correction ", corr, "!")
                        population[rat_index][centroid][coord] = min_bound[centroid][coord]
                    elif population[rat_index][centroid][coord] > max_bound[centroid][coord]:
                        # corr += 1
                        # print("Correction ", corr, "!")
                        population[rat_index][centroid][coord] = max_bound[centroid][coord]
        
        C = 2 * r.random()
        R = r.random() * 4 + 1
        A = R - step * (R / max_steps)

        cluster_assignments = [[[] for _ in range(k)] for _ in range(agents)]
        rat_index = 0

        for rat in population:
            for instance in instances:
                distances = [distance(instance, rat[i]) for i in range(k)]
                cluster = np.argmin(distances)
                cluster_assignments[rat_index][cluster].append(instance)

            fitness = addc(rat, rat_index, distance, cluster_assignments, n)

            if fitness < best:
                best = fitness
                best_rat = rat.copy()
            rat_index += 1
        step += 1
        convergence.append(best)
        # print("Step ", step, ": ", best)
    # plt.plot(convergence)
    # plt.show()
    return population, best_rat, cluster_assignments, convergence

# objective = lambda x: x[0]**2 + x[1]**2

# objective = lambda x: -(x[1] + 47) * math.sin(math.sqrt(abs(x[0] / 2 + (x[1] + 47)))) - x[0] * math.sin(math.sqrt(abs(x[0] - (x[1] + 47))))
# b = rso(100, [-512, -512], [512, 512], objective, 200)
# print(b)

# print("Loading data...")
# tf_idf = pd.read_csv('data/tfidf.csv')
# print("Done.")

# tf_idf = np.array(tf_idf)

# def euc_distance(mp, mj):
#     return np.linalg.norm(mp-mj)

# def cos_distance(mp, mj):
#     return np.dot(mp, mj)/(np.linalg.norm(mp)*np.linalg.norm(mj))

# RSO_ITERATIONS = 50
# n = tf_idf.shape[0]
# k = 5

# population, best_rat, cluster_assignments = rso_clustering(instances=tf_idf,
#         agents=5,
#         k=k,
#         min_bound=np.zeros((k,n)),
#         max_bound=np.ones((k,n)),
#         distance=euc_distance,
#         max_steps=RSO_ITERATIONS
# )