import csv

outlook = ["sunny", "overcast", "rainy", ""]
temperature = ["hot", "mild", "coll", ""]
humidity = ["high", "normal", ""]
windy = ["TRUE", "FALSE", ""]
play = ["no", "yes"]


supp = 0.01
conf = 0.1
count = 0
file = open("CV1/result.txt", "w+")
list_conditions = []

for i in outlook:
    for j in temperature:
        for k in humidity:
            for l in windy:
                # for m in play:
                tmp = i + " " + j + " " + k + " " + l + "\n"
                file.write(tmp)
                count = count + 1

i = 0
positive = 0
negative = 0

file.close()
with open("CV1/result.txt") as f:
    for line in f:
        list_conditions.append(line[:-1])
list_conditions.append("")
for item in list_conditions:
    item = item.split()
    with open("CV1/weather.csv") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            result = all(elem in row for elem in item)
            if result:
                i = i + 1
                if "yes" in row:
                    positive = 1 + positive
                if "no" in row:
                    negative = 1 + negative
        if i != 0:
            if positive > negative and positive / i >= conf and i / 14 > supp:
                print(str(item) + " supp =" + str(i / 14) + ", conf =" + str(positive / i) + ", yes")
            if negative > positive and negative / i >= conf and i / 14 > supp:
                print(str(item) + " supp =" + str(i / 14) + ", conf =" + str(negative / i) + ", no")

    positive = 0
    negative = 0
    i = 0
