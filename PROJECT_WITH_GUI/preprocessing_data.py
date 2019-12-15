import os
import csv


def check_path_exists(path_file):
    if (os.path.exists(path_file)) and path_file[-4:] == ".csv":
        return True
    else:
        return False


def get_names_collumn(filename, separator):
    with open(filename) as f:
        first_line = f.readline()
        first_line = first_line.replace('\n', '')
        first_line = first_line.replace(' ', '')
    words = first_line.split(separator)
    return words


def data_about_input_file(list_data, seperator, filename):
    string_input = f'INPUT: \n Path to file: {filename} \n Seperator: {seperator} \n Number instance: {len(list_data)} \n Number attributes in file: {len(list_data[0])} \nOUTPUT:\n'
    return string_input


def raw_data_as_list(filename, separator):
    list_data = []
    with open(filename) as f:
        for line in f:
            reader = csv.reader(f, delimiter=separator)
            for row in reader:
                list_data.append(row)
    return list_data


def remove_empty_collumn(list_data):
    empty_rows = []
    for item in list_data:
        if '' in item:
            empty_rows.append(item)
    for x in empty_rows:
        list_data.remove(x)
    return list_data


def remove_collumns_in_list(omitted_collumns, list_data, filename, separator):
    main_row = get_names_collumn(filename, separator)
    if omitted_collumns == '':
        pass
    elif ',' in omitted_collumns:
        omite_list = omitted_collumns.split(',')
        try:
            index_list = [main_row.index(item) for item in omite_list]
        except ValueError:
            return -1
        index_list = sorted(index_list, reverse=True)
        for x in index_list:
            for row in list_data:
                row.pop(x)

    else:
        for row in list_data:
            try:
                row.pop(main_row.index(omitted_collumns))
            except ValueError:
                return -1

    for row in list_data:
        for index, item in enumerate(row):
            if not isFloat(item):
                tmp_index = index
                list_data = categorization_attributs(list_data, tmp_index)
                break
    try:
        list_data = [[float(item) for item in row] for row in list_data]
    except ValueError:
        pass
    return list_data


def isFloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def categorization_attributs(list_data, index):
    value_list = []
    new_list = []
    for row in list_data:
        if row[index] not in value_list:
            value_list.append(row[index])
    for row in list_data:
        row_list = []
        for index_item, item in enumerate(row):
            if index_item == index:
                row_list.append(value_list.index(item))
            else:
                row_list.append(float(item))
        new_list.append(row_list)
    return new_list
