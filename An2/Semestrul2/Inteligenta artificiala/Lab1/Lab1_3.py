"""
    Să se determine produsul scalar a doi vectori rari care conțin numere reale.
    Un vector este rar atunci când conține multe elemente nule. Vectorii pot avea
    oricâte dimensiuni. De ex. produsul scalar a 2 vectori unisimensionali [1,0,2,0,3]
    și [1,2,0,3,1] este 4.
"""


# Complextatea temporala: O(n)
# Complextatea spatiala: O(1)
def produs_scalar(v1, v2):
    p = 0
    for i, j in zip(v1, v2):
        p += i * j
    return p


def test():
    assert (produs_scalar([1, 0, 2, 0, 3], [1, 2, 0, 3, 1]) == 4)
    assert (produs_scalar([1, 2, 1], [0, 3, 0]) == 6)
    assert (produs_scalar([0, 2, 0, 3], [5, 5, 7, 0]) == 10)


if __name__ == '__main__':
    test()


# Solutia oferita ce bot:
# Complextatea temporala: O(n)
# Complextatea spatiala: O(1)
"""
    def dot_product_sparse(vec1, vec2):
        if len(vec1) != len(vec2):
            return "Vectorii trebuie să aibă aceeași lungime."

        dot = 0
        for i in range(len(vec1)):
            if vec1[i] != 0 and vec2[i] != 0:
                dot += vec1[i] * vec2[i]
    
        return dot
"""