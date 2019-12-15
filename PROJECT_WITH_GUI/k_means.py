import random
import math
import numpy as np
import sys


def create_centroid(num_centroids, list_data):
    centroids = []

    for _ in range(int(num_centroids)):
        x = random.randint(1, len(list_data) - 1)
        centroid = [list_data[x][j] for j in range(len(list_data[0]))]
        centroids.append(centroid)
    return centroids


def add_node_to_clusters(centroids, num_centroids, list_data):
    list_clusters = [[] for _ in range(int(num_centroids))]
    for item_data in list_data:
        x = []
        for item_cluster in centroids:
            x.append(distance(item_cluster, item_data))
        index = x.index(min(x))
        list_clusters[index].append(item_data)
    return list_clusters


def distance(node1, node2):
    dist = [(node1[i] - node2[i]) ** 2 for i in range(len(node1))]
    return math.sqrt(sum(dist))


def cal_centroid(num_centroids, cluster):
    new_centroid = [[] for _ in range(int(num_centroids))]
    for i in range(int(num_centroids)):
        for x in range(len(cluster[0][0])):
            mean_cluster = [0] * len(cluster[0][0])
            for item in range(len(cluster[i])):
                mean_cluster[x] += cluster[i][item][x]
            if len(cluster[i]) != 0:
                new_centroid[i].append(mean_cluster[x] / len(cluster[i]))
            else:
                new_centroid[i].append(0)
    return new_centroid


def k_means(list_data, num_clusters, iter):
    f_data = []
    SSE_length = sys.maxsize
    for i in range(int(iter)):
        sum = 1
        centroids = create_centroid(num_clusters, list_data)
        last_centroids = centroids

        while True:
            sum += 1
            clusters = add_node_to_clusters(centroids, num_clusters, list_data)
            centroids = cal_centroid(num_clusters, clusters)
            # print([[np.round(i, 2) for i in item] for item in centroids])  # rounded centroids only for print
            # print(centroids)
            if centroids != last_centroids:
                last_centroids = centroids
            else:
                f_centroid = [[np.round(i, 2) for i in item] for item in centroids]
                data = [f_centroid, clusters, sum]
                SSE_current = SSE(f_centroid, clusters, num_clusters)
                if SSE_length > SSE_current:
                    SSE_length = SSE_current
                    f_data = [f_centroid, clusters, sum]
                break
    return f_data[0], f_data[1], f_data[2]

def SSE(centroids, clusters, num_clusters):
    total_sum_SSE = 0
    for i in range(int(num_clusters)):
        m = 0
        for x in clusters[i]:
            m += distance(x, centroids[i])
            total_sum_SSE += m
        print(f"Cluster {i + 1}:")
        print(f"Element in cluster: {len(clusters[i])}")
        print("")
    return total_sum_SSE
