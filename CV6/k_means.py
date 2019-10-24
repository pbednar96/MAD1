import csv
import matplotlib.pyplot as plt
import math
import numpy as np
import random

FILENAME = "iris.csv"
NUM_CLUSTERS = 4
NUM_PARAMS = 4


def get_list():
    list_data = []
    with open(FILENAME) as f:
        for line in f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                list_data.append(row)
    return list_data


# def show_scatter(list_data):
#     first_column = []
#     second_column = []
#     for i in list_data:
#         first_column.append(float(i[0]))
#         second_column.append(float(i[1]))
#     plt.xlabel('x2 sepal width')
#     plt.ylabel('x2 sepal length')
#     plt.axis([4, 8.5, 1.5, 5])
#     plt.scatter(first_column, second_column)
#     plt.show()


def preprocessing_data(raw_data):
    final_list = []
    for i in raw_data:
        final_list.append([float(i[0]), float(i[1]), float(i[2]), float(i[3])])
    return final_list


def distance(node1, node2):
    return math.sqrt(((node1[0] - node2[0]) ** 2) + ((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2) + (
            (node1[3] - node2[3]) ** 2))


def create_centroid(num_centroids, list_data):
    centroids = []
    for i in range(num_centroids):
        x = random.randint(1, len(list_data) - 1)
        centroids.append([list_data[x][0], list_data[x][1], list_data[x][2], list_data[x][3]])
    return centroids


def cal_centroid(num_centroids, cluster):
    final_list = [[] for _ in range(NUM_CLUSTERS)]
    for i in range(num_centroids):
        for x in range(NUM_PARAMS):
            mean_cluster = [0, 0, 0, 0]
            for item in range(len(cluster[i])):
                mean_cluster[x] += cluster[i][item][x]
            final_list[i].append(mean_cluster[x] / len(cluster[i]))
    return final_list


def add_node_to_clusters(clusters, list_data):
    list_clusters = [[] for _ in range(NUM_CLUSTERS)]
    for item_data in list_data:
        x = []
        for item_cluster in clusters:
            x.append(distance(item_cluster, item_data))
        index = x.index(min(x))
        list_clusters[index].append(item_data)
    return list_clusters


def SSE(centroids, clusters, num_clusters):
    total_sum_SSE = 0
    for i in range(num_clusters):
        m = 0
        for x in clusters[i]:
            m += distance(x, centroids[i])
            total_sum_SSE += m
        print(f"Cluster {i + 1}:")
        print(f"SSE value: {m}")
        print(f"Element in cluster: {len(clusters[i])}")
        print("")
    print(f'Sum SSE:{total_sum_SSE}')


def main():
    list_data = preprocessing_data(get_list())
    centroids = create_centroid(NUM_CLUSTERS, list_data)
    print(centroids)
    last_centroids = centroids
    while True:
        clusters = add_node_to_clusters(centroids, list_data)
        centroids = cal_centroid(NUM_CLUSTERS, clusters)
        print([[np.round(i, 2) for i in item] for item in centroids])  # rounded centroids only for print print
        if centroids != last_centroids:
            last_centroids = centroids
        else:
            break
    print("SSE for centroids:")
    SSE(centroids, clusters, NUM_CLUSTERS)


if __name__ == "__main__":
    main()
