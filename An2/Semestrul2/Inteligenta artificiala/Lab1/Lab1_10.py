"""
    Considerându-se o matrice cu n x m elemente binare (0 sau 1) sortate crescător
    pe linii, să se identifice indexul liniei care conține cele mai multe elemente de 1.
    De ex. în matricea
    [[0,0,0,1,1],
     [0,1,1,1,1],
     [0,0,1,1,1]]
    a doua linie conține cele mai multe elemente 1.
"""


# Complextatea temporala: O(n * logm)
# Complextatea spatiala: O(1)
def cautare_binara(lista):
    stanga = 0
    dreapta = len(lista) - 1
    rezultat = -1

    while stanga <= dreapta:
        mijloc = (stanga + dreapta) // 2
        if lista[mijloc] == 1:
            rezultat = mijloc
            dreapta = mijloc - 1
        else:
            stanga = mijloc + 1

    return rezultat


def index_nr_max1(matr):
    nr_lin = len(matr)
    nr_col = len(matr[0]) if nr_lin > 0 else 0

    linie_max1 = 0
    max1 = 0

    for i in range(nr_lin):
        for j in range(nr_col):
            index = cautare_binara(matr[i])
            if index != -1 and nr_col - index > max1:
                max1 = nr_col - index
                linie_max1 = i

    return linie_max1


def test():
    assert (index_nr_max1([[0, 0, 0, 1, 1],
                           [0, 1, 1, 1, 1],
                           [0, 0, 1, 1, 1]]) == 1)
    assert (index_nr_max1([[0, 0, 0, 0, 1],
                           [0, 0, 0, 1, 1],
                           [0, 0, 1, 1, 1]]) == 2)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n * m)
# Complextatea spatiala: O(1)
"""
    def line_with_most_ones(matrix):
        num_rows = len(matrix)
        num_columns = len(matrix[0]) if num_rows > 0 else 0
    
        max_ones_row_index = 0
        max_ones_count = 0
    
        for i in range(num_rows):
            ones_count = sum(matrix[i])
            if ones_count > max_ones_count:
                max_ones_count = ones_count
                max_ones_row_index = i
    
        return max_ones_row_index
"""
