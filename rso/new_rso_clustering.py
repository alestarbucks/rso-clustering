import numpy as np
import random as r
import tqdm
import time

# IMPLEMENTS A DIFFERENT VERSION OF RAT SWARM OPTIMIZATION FOR CLUSTERING
# THAT UPDATES THE POSITIONS DIFFERENTLY
# NOT CONSIDERED FOR THE RESULTS IN THE PAPER

def addc(centroids, distance, cluster_assignments):
    """ADDC: Average Distance to Cluster Centroid"""

    cluster_index = 0
    fitness = 0

    for cluster_index in range(len(cluster_assignments)):
        if len(cluster_assignments[cluster_index]) == 0: continue

        aux = 0

        for instance in cluster_assignments[cluster_index]:
            aux += distance(centroids[cluster_index], instance)
        
        fitness += aux/len(cluster_assignments[cluster_index])
    
    return fitness/len(centroids)

def rso_clustering(instances, agents, k, min_bound, max_bound, distance, max_steps):
    start_time = time.time()
    population = []

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

        fitness = addc(rat, distance, cluster_assignments[rat_index])
        if fitness < best:
            best = fitness
            best_rat = rat.copy()
        rat_index += 1
    
    convergence.append([time.time() - start_time, best])

    step = 0

    C = 2 * r.random()
    R = r.random() * 4 + 1
    A = R * (1 - (step / max_steps))

    for step in tqdm.tqdm(range(max_steps)):
        for rat_index in range(agents):
            informed_position = A * population[rat_index] + (C * (best_rat - population[rat_index]))
            population[rat_index] = (best_rat - informed_position)
            
            for centroid in range(k):
                for coord in range(min_bound.shape[1]):
                    if population[rat_index][centroid][coord] < min_bound[centroid][coord]:
                        population[rat_index][centroid][coord] = min_bound[centroid][coord]
                    elif population[rat_index][centroid][coord] > max_bound[centroid][coord]:
                        population[rat_index][centroid][coord] = max_bound[centroid][coord]
        
        C = 2 * r.random()
        R = r.random() * 4 + 1
        A = R * (1 - (step / max_steps))

        cluster_assignments = [[[] for _ in range(k)] for _ in range(agents)]
        rat_index = 0

        for rat in population:
            for instance in instances:
                distances = [distance(instance, rat[i]) for i in range(k)]
                cluster = np.argmin(distances)
                cluster_assignments[rat_index][cluster].append(instance)

            fitness = addc(rat, distance, cluster_assignments[rat_index])

            if fitness < best:
                best = fitness
                best_rat = rat.copy()
            rat_index += 1
        step += 1
        convergence.append([time.time() - start_time, best])
    return population, best_rat, cluster_assignments, convergence