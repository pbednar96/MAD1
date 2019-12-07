import numpy as np
import random
import sys

SIZE = 550


def create_martix_nodes(size):
    matrix = np.zeros((size, size))
    return matrix


def generate_edges( propability, size):
    matrixx = create_martix_nodes(size)
    for i in range(size):
        for j in range(size):
            r = random.uniform(0, 1)
            if r < propability and i != j:
                matrixx[i][j] = 1
    return matrixx


def get_degree_in_subgraphs(matrix, size):
    sum_all_degree = 0
    list_coefficients = []
    for s in range(size):
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
            # print(f'{s}: {coefficient}')
            sum_all_degree += coefficient
            list_coefficients.append(coefficient)
        else:
            pass
            # print(f'{s}: 0.0')
            # list_coefficients.append(0)
    return sum_all_degree, list_coefficients


def floyd_alg(matrix):
    x = matrix
    len_matrix = len(x)
    x = np.where(x == 0, sys.maxsize, x)
    for k in range(len_matrix):
        for i in range(len_matrix):
            for j in range(len_matrix):
                if x[i][j] > x[i][k] + x[k][j]:
                    x[j][i] = x[i][j] = x[i][k] + + x[k][j]
    return x


def degree_graph(matrix, size):
    list_value = [0] * size
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                list_value[i] = list_value[i] + 1
    return list_value


def main():

    # <d> < 1
    matrix_1 = generate_edges(0.0008, SIZE)
    print(f'Count edge: {sum(degree_graph(matrix_1, SIZE))}')
    sum_edge = sum(degree_graph(matrix_1, SIZE))
    print(sum_edge/SIZE)
    # sum_coef, list_coef = get_degree_in_subgraphs(matrix_1, SIZE)
    # print(list_coef)

    #<d> = 1
    matrix_2 = generate_edges(0.0018, SIZE)
    print(f'Count edge: {sum(degree_graph(matrix_2, SIZE))}')
    sum_edge = sum(degree_graph(matrix_2, SIZE))
    print(sum_edge/SIZE)
    # sum_coef, list_coef = get_degree_in_subgraphs(matrix_2, SIZE)
    # print(list_coef)

    # <d> < 1
    matrix_3 = generate_edges(0.004, SIZE)
    print(f'Count edge: {sum(degree_graph(matrix_3, SIZE))}')
    sum_edge = sum(degree_graph(matrix_3, SIZE))
    print(sum_edge/SIZE)
    # sum_coef, list_coef = get_degree_in_subgraphs(matrix_3, SIZE)
    # print(list_coef)


if __name__ == "__main__":
    main()


# Id - Unikatní ID for každou prodanou nemovitost
# Date - Datum prodeje nemovitosti
# Price - Cena za každý prodanou nemovitost
# Bedrooms - Počet ložnic
# Bathrooms - Počet koupelen, kde .5 hodnota znamená místnost s toaletou bez sprchy
# Sqft_living - Vnitřní obytná plocha
# Sqft_lot - Plocha parcely
# Floors - Počet pater
# Waterfront - hodnoty <0,1>, zda dům má výhed na nábřeží nebo ne
# View - index <0,4>, jak dobrý je výhled na nemovitost
# Condition - index <1,5>, stav nemovitosti
# Grade - index <1,13>, kde 1-3 nemovitost nevyhovuje konstrukci nebo designem, 7 průměrná hodnota urovně kontrukce a designu, 11-13 má výsokou kvalitu konstrukce a designu
# Sqft_above - obytná plocha nad zemi
# Sqft_basement - obytná plocha v podzemí
# yr_built - rok, kdy byl dům postaven
# yr_renovated - rok, kdy byl poslední renovace
# zip_code - zipcode
# Lat - zeměpisna šířka
# Long - zeměpisná výška
# Sqft_living15 - zanedbatelný parametr
# Sqft_lot15 - zanedbatelný parametr

