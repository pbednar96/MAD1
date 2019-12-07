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


def get_degree_in_subgraphs(matrix):
    sum_all_degree = 0
    list_coefficients = []
    for s in range(34):
        x = matrix[s]
        m = []
        sum = 0
        for position, item in enumerate(x):
            if item == 1:
                m.append(position)
        for i in m:
            for j in m:
                if matrix[i][j] == 1 and i != j:
                    sum += 1
        tr = int(len(m)) * (int(len(m)) - 1)
        if (tr != 0):
            coefficient = (2 * int(sum / 2)) / tr
            print(f'{s}: {coefficient}')
            sum_all_degree += coefficient
            list_coefficients.append(coefficient)
        else:
            print(f'{s}: 0.0')
            list_coefficients.append(0)
    return sum_all_degree, list_coefficients


def global_cluster_coefficient(degree):
    return degree / 34


def degree_graph():
    matrix = create_matrix()
    list_value = [0] * 34
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list_value[i] = list_value[i] + 1
    return list_value


def clustering_efect(list_coefficients):
    x = degree_graph()
    final_list = []
    list_degree = []
    for i in range(34):
        ss = 0
        for j in range(34):
            if i == x[j]:
                ss += list_coefficients[j]
        if(x.count(i)) != 0:
            print(f'{i}: {ss/(x.count(i))}')
            final_list.append(ss/(x.count(i)))
            list_degree.append(i)
        else:
            print(f'{i}: 0.0')

    return final_list, list_degree



def main():
    x = create_matrix()
    print("-----------Local_CC-----------")
    s, list_coeff = get_degree_in_subgraphs(x)
    print("-----------Global_CC-----------")
    print(f'Global coefficient: {global_cluster_coefficient(s)}')
    print("-----------Graph-----------")
    scat, point = clustering_efect(list_coeff)
    print(scat)
    print(point)
    plt.scatter(point, scat)


    plt.show()


if __name__ == "__main__":
    main()
