"""
10. Se dă o listă de numere întregi a1,...an, determinați toate sub-secvențele cu lungime mai mare decât 2 cu
proprietatea că: numerele sunt în ordine crescătoare şi numerele consecutive au cel puţin o cifră în comun.
"""


def citire():
    """
    Citeste n (lungimea listei) si lista data
    :return a:list
    """
    while True:
        try:
            n = int(input("n = "))
            if n <= 1:
                raise ValueError
        except ValueError:
            print("Dati un numar natural >1 pentru n")
            continue
        break
    a = []
    print("Dati cele", n, "numere intregi: ")
    for i in range(n):
            m = int(input("Dati un numar intreg: "))
            a.append(m)
    return a


def cifra_comuna(a, b):
    """
    Determina daca numerele intregi a si b au cel putin o cifra comuna
    :type a: int
    :type b: int
    :return: True in cazul in care numerele au cel putin o cifra comuna, altfel False
    """
    if a < 0:
        a = a * (-1)
    if b < 0:
        b = b * (-1)
    while a > 0:
        cif = a % 10
        a = int(a / 10)
        cop = b
        while cop > 0:
            if cif == cop % 10:
                return True
            cop = int(cop / 10)
    return False


def consistent(x):
    if len(x) == 1:
        return True
    for i in range(1, len(x)):
        if (x[i] <= x[i - 1]) or (cifra_comuna(x[i], x[i - 1]) is False):
            return False
    return True


def solution(x):
    return len(x) >= 2


def backtrack_recursiv(x, n, k, lista):
    if k == n:
        return
    else:
        x.append(-1)
        for value in lista:
            x[-1] = value
            if consistent(x):
                if solution(x):
                    print(x)
                backtrack_recursiv(x[:], n, k + 1, lista)


def consistent_iter(x, n, lista):
    if len(x) == 1:
        return True
    if len(x) > n:
        return False

    for i in range(1, len(x)):
        if (lista[x[i]] <= lista[x[i - 1]]) or (cifra_comuna(lista[x[i]], lista[x[i - 1]]) is False):
            return False
    return True


def solution_iter(x):
    return len(x) >= 2


def output_solution_iter(x, lista):
    sol = [lista[i] for i in x]
    print(sol)


def backtrack_iterativ(n, lista):
    x = [-1]
    while len(x) > 0:
        chosen = False
        while not chosen and x[-1] < n - 1:
            x[-1] = x[-1] + 1
            chosen = consistent_iter(x, n, lista)
        if chosen is True:
            if solution_iter(x):
                output_solution_iter(x, lista)
            x.append(-1)
        else:
            x = x[:-1]


def main():
    """
    Entry point.
    Console UI.
    """
    while True:
        print("1. Recursiv")
        print("2. Iterativ")
        print("x. Exit")
        cmd = input("    Dati comanda: ")
        if cmd == 'x':
            print("Multumim ca ati utilizat aplicatia! :)")
            return
        elif cmd == '1':
            lista = citire()
            n = len(lista)
            backtrack_recursiv([], n,  0, lista)
        elif cmd == "2":
            lista = citire()
            n = len(lista)
            backtrack_iterativ(n, lista)
        else:
            print("Comanda gresita!")
            continue


# if __name__ == '__main__':
#    main()

# n = 6
# l = [1, 12, 423, 10, 3, 9]

n = 7
l = [-13, 478, 53, 679, -47, 82, 5]

backtrack_recursiv([], n,  0, l)
print('-------------------')
backtrack_iterativ(n, l)
