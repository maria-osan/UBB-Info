from random import sample
from math import factorial, perm, comb
from itertools import permutations, combinations


class Permutation:
    def __init__(self, lista):
        self.lista = lista

    def permutation(self):
        for perm in self.lista:
            for p in permutations(perm):
                print(p)

    def permutation_number(self):
        for p in self.lista:
            print(factorial(len(p)))

    def random_permutation(self):
        for p in self.lista:
            print(sample(p, len(p)))

    def aranjamente(self, nr):
        for perm in self.lista:
            for p in permutations(perm, nr):
                print(p)

    def number_aranjamente(self, nr):
        for p in self.lista:
            print(perm(len(p), nr))

    def random_aranjamente(self, nr):
        for p in self.lista:
            print(sample(p, nr))

    def combinari(self, nr):
        for perm in self.lista:
            for p in combinations(perm, nr):
                print(p)

    def number_combinari(self, nr):
        for p in self.lista:
            print(comb(len(p), nr))

    def random_combinari(self, nr):
        for perm in self.lista:
            for p in sorted(sample(range(len(perm)), nr)):
                print(perm[p], end="")


clasa = Permutation(["word"])
clasa.random_combinari(2)
