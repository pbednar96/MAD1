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


def raw_data_as_list(filename, separator):
    list_data = []
    with open(filename) as f:
        for line in f:
            reader = csv.reader(f, delimiter=separator)
            for row in reader:
                list_data.append(row)
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
    try:
        list_data = [[float(item) for item in row] for row in list_data]
    except ValueError:
        pass
    return list_data
