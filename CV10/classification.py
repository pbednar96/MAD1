import csv
import math
import static_file
from copy import deepcopy as dp

FILENAME = "iris.csv"
NUM_CLUSTERS = 4
NUM_PARAMS = 4

list_results = static_file.list_results


def get_list():
    list_data = []
    with open(FILENAME) as f:
        for line in f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                list_data.append(row)
    return list_data


def distance(node1, node2):
    return math.sqrt(((node1[0] - node2[0]) ** 2) + ((node1[1] - node2[1]) ** 2) + ((node1[2] - node2[2]) ** 2) + (
            (node1[3] - node2[3]) ** 2))


def preprocessing_data(raw_data):
    final_list = []
    for i in raw_data:
        final_list.append([float(i[0]), float(i[1]), float(i[2]), float(i[3]), i[4]])
    return final_list


def find_nearest_in_list(k, input_data):
    sorted_list_by_distance = sorted(input_data, key=lambda x: x[5])
    return sorted_list_by_distance[:k]


def K_NN(k_range, input_data, data):
    data_with_distinct = dp(data)
    for i in data_with_distinct:
        i.append(distance(i, input_data))
    data_in_k_range = find_nearest_in_list(k_range, data_with_distinct)
    list_value = [item[4] for item in data_in_k_range]
    print(list_value)
    tmp = []
    for item in list_results:
        tmp.append(list_value.count(item))

    prediction = list_results[tmp.index(max(tmp))]
    return prediction


def k_fold_cross_validation(raw_input):
    pass



def main():
    list_data = preprocessing_data(get_list())
    print(list_data)
    x = K_NN(10, [1,1,5.6,2.4], list_data)
    print(x)



if __name__ == "__main__":
    main()
