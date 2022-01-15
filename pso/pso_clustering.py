import numpy as np
import random
import time
import tqdm

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

def pso_clustering(k, data, distance, n_particles=50, w=0.72, c1=1.49, c2=1.49, max_iter=100):
    start_time = time.time()
    convergence = []
    
    particles = [random.sample(list(data), k) for _ in range(n_particles)]
    velocities = np.zeros(n_particles)

    global_best = None
    global_best_fitness = np.Inf

    for step in tqdm.tqdm(range(max_iter - 1)):
        fitness = []
        cluster_assignments = [[[] for i in range(k)] for j in range(n_particles)]
        print("A")

        for particle_index in range(n_particles):
            print("AA")
            for instance in data:
                distances = [distance(instance, centroid) for centroid in particles[particle_index]]
                cluster_assignments[particle_index][np.argmin(distances)].append(instance)

                fitness.append(addc(particles[particle_index], distance, cluster_assignments[particle_index]))

        current_best_index = np.argmin(fitness)
        current_best = particles[current_best_index]
        current_best_fitness = fitness[current_best_index]

        if current_best_fitness < global_best_fitness:
            global_best = current_best
            global_best_fitness = current_best_fitness

        print("C")

        for particle_index in range(n_particles):
            inertia = w * velocities[particle_index]
            current_best_contribution = c1 * random.random() * (current_best - particles[particle_index])
            global_best_contribution = c2 * random.random() * (global_best - particles[particle_index])
            
            velocities[particle_index] = inertia + current_best_contribution + global_best_contribution
            
            particles[particle_index] += velocities[particle_index]
        
        print("D")

        convergence.append(time.time() - start_time, global_best_fitness)

    for particle_index in range(n_particles):
        cluster_assignments = [[] for _ in range(k)]

        for instance in data:
            distances = [distance(instance, centroid) for centroid in particles[particle_index]]
            cluster_assignments[np.argmin(distances)] = instance

            fitness.append(addc(particles[particle_index], distance, cluster_assignments))

    current_best_index = np.argmin(fitness)
    current_best = particles[current_best_index]
    current_best_fitness = fitness[current_best_index]

    if current_best_fitness < global_best_fitness:
        global_best = current_best
        global_best_fitness = current_best_fitness
    
    convergence.append([time.time() - start_time, global_best_fitness])

    return global_best, convergence, particles