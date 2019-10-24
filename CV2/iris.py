import csv
import numpy as np
import math
import matplotlib.pyplot as plt
import statistics
import scipy.stats


def get_list():
    list_data = []
    with open("iris.csv") as f:
        for line in f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                list_data.append(row)
    return list_data


def distance(sepal_x, sepal_y, petal_x, petal_y):
    return math.sqrt((sepal_x * sepal_y) + (petal_x * petal_y))


def count_frequency(list_data):
    freq = {}
    for item in list_data:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    return freq


# smerodatna odchylka ... spocita se z rozptilu ...
# vezmy Iris data set ... spocitam cestnost

def show_histogram(dict):
    plt.bar(list(dict.keys()), dict.values(), color='g')
    plt.show()


def normal_distribution(list_data):
    mean = statistics.mean(list_data)
    std = statistics.variance(list_data)
    y = scipy.stats.norm.pdf(list_data, mean, std)

    plt.plot(list_data, y, color='black')

    plt.show()


def emprirical_rule(list_data):
    fr_count = count_frequency(list_data)
    for key, value in fr_count.items():
        fr_count[key] = fr_count[key] / 150
    show_histogram(fr_count)


def function_for_data(list_data):
    emprirical_rule(list_data)

    print("Mean:" + str(statistics.mean(list_data)))
    print("Variance" + str(statistics.variance(list_data)))


def main():
    list_data = get_list()
    sepal_length = []
    sepal_width = []
    petal_length = []
    petal_width = []
    dist = []

    for i in list_data:
        sepal_length.append(float(i[0]))
        sepal_width.append(float(i[1]))
        petal_length.append(float(i[2]))
        petal_width.append(float(i[3]))

    for i in range(len(sepal_length)):
        dist.append(
            distance(float(sepal_length[i]), float(sepal_width[i]), float(petal_length[i]), float(petal_width[i])))

    emprirical_rule(sepal_length)
    normal_distribution(sepal_length)


if __name__ == "__main__":
    main()
