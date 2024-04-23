"""
    Să se determine distanța Euclideană între două locații
    identificate prin perechi de numere. De ex. distanța
    între (1,5) și (4,1) este 5.0
"""
from math import sqrt


# Complextatea temporala: O(1)
# Complextatea spatiala: O(1)
class Punct:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanta(self, punct):
        return sqrt((punct.x - self.x) ** 2 + (punct.y - self.y) ** 2)


def test():
    punct1 = Punct(1, 5)
    punct2 = Punct(4, 1)
    assert (punct1.distanta(punct2) == 5.0)
    punct1 = Punct(3, 5)
    punct2 = Punct(2, 3)
    assert (punct1.distanta(punct2) == sqrt(5))
    punct1 = Punct(7, 9)
    punct2 = Punct(1, 1)
    assert (punct1.distanta(punct2) == 10)


if __name__ == '__main__':
    test()

# Solutia oferita ce bot:
# Complextatea temporala: O(1)
# Complextatea spatiala: O(1)
"""
    def euclidean_distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""