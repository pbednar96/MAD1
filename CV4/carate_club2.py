import csv
import numpy as np
import sys
import matplotlib.pyplot as plt

np.set_printoptions(threshold=sys.maxsize)

FILE_NAME = "KarateClub.csv"


def create_list_from_csv():
    list_data = []
    with open(FILE_NAME) as f:
        for line in f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                list_data.append(row)
    return list_data


def create_txt_from_list():
    x = create_list_from_csv()
    file = open("result.txt", "w+")
    for j in range(34):
        file.write(str(j + 1) + ": ")
        for i in range(len(x)):
            if str(x[i][0]) == str(j + 1):
                file.write(str(x[i][1]) + ", ")
        for i in range(len(x)):
            if str(x[i][1]) == str(j + 1):
                file.write(str(x[i][0]) + ", ")
        file.write("\n")


def create_matrix():
    matrix = np.zeros((34, 34))
    # matrix = [[0] * 34] * 34
    list = create_list_from_csv()
    for i in range(len(list)):
        a = int(list[i][0]) - 1
        b = int(list[i][1]) - 1
        matrix[a, b] = 1
        matrix[b, a] = 1

    matrix.tolist()
    return matrix


def create_list():
    dict = {}
    list = create_list_from_csv()
    for j in range(len(list)):
        for i in range(34):
            if list[j][1] == i:
                print(list[j][1])


def result_as_file():
    f = open("result.txt", "w+")
    f.write(str(create_matrix()))


def degree_graph():
    matrix = create_matrix()
    list_value = [0] * 34
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list_value[i] = list_value[i] + 1
    return list_value


def minimum():
    list_value = degree_graph()
    minim = min(list_value)
    x = 0
    for item in range(len(list_value)):
        if list_value[item] == minim:
            x = item
    return x


def maximum():
    list_value = degree_graph()
    maximum = max(list_value)
    x = 0
    for item in range(len(list_value)):
        if list_value[item] == maximum:
            x = item
    return x


def Average():
    list_value = degree_graph()
    return sum(list_value) / len(list_value)



def floyd_alg():
    x = create_matrix()
    len_matrix = len(x)
    x = np.where(x == 0, sys.maxsize, x)
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                if x[i][j] > x[i][k] + x[k][j]:
                    x[j][i] = x[i][j] = x[i][k] + + x[k][j]
    return x


def closeness_centrality():
    x = floyd_alg()
    len_array = len(create_matrix()) +1
    list_closeness = []
    for i in range(34):
        list_closeness.append([i+1,35/np.sum(x[i])])
    return list_closeness

# create_txt_from_list()
#
# print("Minimum is n.: " + str(minimum()))
# print("Maximum is n.: " + str(maximum()))
# print("Avg is : " + str(Average()))
#
# show_histogram()

print(closeness_centrality())
