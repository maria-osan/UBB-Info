"""
    Considerându-se o matrice cu n x m elemente întregi și o listă
    cu perechi formate din coordonatele a 2 căsuțe din matrice
    ((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricile
    identificate de fieare pereche.
"""


# Complextatea temporala: O(n * m)
# Complextatea spatiala: O(1)
def suma_elem_submatr(matr, pairs):
    p, q = pairs[0]
    r, s = pairs[1]
    sum = 0
    for i in range(p, r+1):
        for j in range(q, s+1):
            sum += matr[i][j]
    return sum


def test():
    assert (suma_elem_submatr([[0, 2, 5, 4, 1],
                               [4, 8, 2, 3, 7],
                               [6, 3, 4, 6, 2],
                               [7, 3, 1, 8, 3],
                               [1, 5, 7, 9, 4]], ((2, 2), (4, 4))) == 44)
    assert (suma_elem_submatr([[0, 2, 5, 4, 1],
                               [4, 8, 2, 3, 7],
                               [6, 3, 4, 6, 2],
                               [7, 3, 1, 8, 3],
                               [1, 5, 7, 9, 4]], ((1, 1), (3, 3))) == 38)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(n * m)
# Complextatea spatiala: O(k), unde k este numarul de perechi de coordonate
"""
    def precompute_matrix_sum(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        precomputed = [[0] * cols for _ in range(rows)]
    
        # Calculăm suma pentru prima coloană
        for i in range(rows):
            precomputed[i][0] = matrix[i][0]
    
        # Calculăm suma pentru prima linie
        for j in range(1, cols):
            precomputed[0][j] = precomputed[0][j - 1] + matrix[0][j]
    
        # Calculăm suma pentru restul matricei
        for i in range(1, rows):
            for j in range(1, cols):
                precomputed[i][j] = precomputed[i - 1][j] + precomputed[i][j - 1] - precomputed[i - 1][j - 1] + matrix[i][j]
    
        return precomputed
    
    def calculate_submatrix_sum(precomputed, pair):
        p, q = pair[0]
        r, s = pair[1]
    
        top_left_sum = precomputed[r][s]
        top_right_sum = 0 if q == 0 else precomputed[r][q - 1]
        bottom_left_sum = 0 if p == 0 else precomputed[p - 1][s]
        common_sum = 0 if (p == 0 or q == 0) else precomputed[p - 1][q - 1]
    
        return top_left_sum - top_right_sum - bottom_left_sum + common_sum
    
    def calculate_sum_for_pairs(matrix, pairs):
        precomputed = precompute_matrix_sum(matrix)
        sums = []
        for pair in pairs:
            submatrix_sum = calculate_submatrix_sum(precomputed, pair)
            sums.append(submatrix_sum)
        return sums
"""