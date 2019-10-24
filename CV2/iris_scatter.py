import matplotlib.pyplot as plt
import csv

# s = open("iris.csv").read()
# s =  s.replace(',','.')
# f = open("iris.csv", "w")
# f.write(s)
# f.close()

list_data = []
with open("iris.csv") as f:
    for line in f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            list_data.append(row)

print(list_data)

first_column = []
second_column = []
th_column = []
for i in list_data:
    first_column.append(float(i[0]))
    second_column.append(float(i[1]))
    th_column.append(float(i[2]))

plt.xlabel('x2 sepal width')
plt.ylabel('x2 sepal length')
plt.axis([4, 8.5, 1.5, 5])
plt.scatter(first_column, second_column)
plt.show()

plt.axis([3, 8, 0, 8])
plt.scatter(first_column, th_column)
plt.show()