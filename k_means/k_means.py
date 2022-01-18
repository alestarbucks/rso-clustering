import numpy as np
import random
import tqdm
import time

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

def k_means(k, data, distance, max_iter=100):
    start_time = time.time()
    convergence = []
    
    # randomly select k documents to be the initial centroids
    centroids = random.sample(list(data), k)
    distances = [[] for _ in range(data.shape[0])]

    # main loop
    for step in tqdm.tqdm(range(max_iter)):
        # reset cluster assignments
        cluster_assignments = [[] for _ in range(k)]
        
        # assign each instance to the closest centroid
        for instance_index in range(data.shape[0]):
            distances[instance_index] = [distance(data[instance_index], centroid) for centroid in centroids]
            cluster_assignments[np.argmin(distances[instance_index])].append(data[instance_index])

        # if there is a cluster with no assigned documents,
        # select the farthest point from the biggest cluster and reassign it to the empty cluster's centroid
        clusters_sizes = [len(i) for i in cluster_assignments]
        
        if 0 in clusters_sizes:
            biggest_cluster = np.argmax(clusters_sizes)
            
            for centroid_index in range(k):
                if len(cluster_assignments[centroid_index]) == 0:
                    cluster_distances = np.array(distances)[:, biggest_cluster]
                    moved_instance = cluster_assignments[biggest_cluster].pop(np.argmax(cluster_distances, axis=0))
                    cluster_assignments[centroid_index].append(moved_instance)

        # recompute the centroids 
        for centroid_index in range(k):
            n_instances = len(cluster_assignments[centroid_index])
            if n_instances > 1:
                centroids[centroid_index] = np.sum(cluster_assignments[centroid_index], axis=0)/n_instances
            else:
                centroids[centroid_index] = cluster_assignments[centroid_index][0]

        convergence.append([time.time() - start_time, addc(centroids, distance, cluster_assignments)])

    return centroids, cluster_assignments, convergence