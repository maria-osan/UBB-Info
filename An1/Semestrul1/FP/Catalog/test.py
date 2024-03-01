# varianta cu 2 key
def swap(lista, poz1, poz2):
    """
    Functia interschimba elementele de pe pozitiile date din lista.
    :param lista: lista
    :param poz1: numar intreg
    :param poz2: numar intreg
    """
    tmp = lista[poz1]
    lista[poz1] = lista[poz2]
    lista[poz2] = tmp
    return lista


def selection_sort(lista, *, key=lambda x: x, key2=lambda x: x, reverse=False, reverse2=False):
    """
    Implementarea algoritmului de sortare Selection sort
    :param lista: lista
    :param key: functie dupa care se face sortarea
    :param key2: a doua functie dupa care se face sortarea
    :param reverse: metoda dupa care se face storarea (True - crescator, False - descrescator)
    :param reverse2: metoda dupa care se face storarea (True - crescator, False - descrescator)
    :return list: lista sortata
    """
    for i in range(0, len(lista) - 1):
        ind = i
        if reverse is False:  # sortare crescatoare dupa primul criteriu
            # cauta cel mai mic element din restul listei
            for j in range(i + 1, len(lista)):
                if key(lista[j]) < key(lista[ind]):
                    ind = j
                elif key(lista[j]) == key(lista[ind]):
                    if reverse2 is False:  # sortare crescatoare dupa al doilea criteriu
                        if key2(lista[j]) < key2(lista[ind]):
                            ind = j
                    else:  # sortare descrescatoare dupa al doilea criteriu
                        if key2(lista[j]) > key2(lista[ind]):
                            ind = j
            if i < ind:
                # interschimbare elemente
                swap(lista, i, ind)

        elif reverse is True:  # sortare descrescatoare dupa primul criteriu
            # cauta cel mai mare element din restul listei
            for j in range(i + 1, len(lista)):
                if key(lista[j]) > key(lista[ind]):
                    ind = j
                elif key(lista[j]) == key(lista[ind]):
                    if reverse2 is False:  # sortare crescatoare dupa al doilea criteriu
                        if key2(lista[j]) < key2(lista[ind]):
                            ind = j
                    else:  # sortare descrescatoare dupa al doilea criteriu
                        if key2(lista[j]) > key2(lista[ind]):
                            ind = j
            if i < ind:
                # interschimbare elemente
                swap(lista, i, ind)
    return lista


# varianta cu functia de comparare
def cmp(x, y):
    if y[0] < x[0]:
        return True
    elif x[0] == y[0] and y[1] > x[1]:
        return True
    else:
        return False


def selectionsort(lista):
    """
    Implementare Selection sort
    :param lista: lista care va fi sortata
    :return: returneaza lista sortata
    """

    n = len(lista)
    for i in range(n-1):
        for j in range(i+1, n):
            if cmp((lista[i]), (lista[j])):
                swap(lst, i, j)
    return lista


# lst = [1, 5, 3, 15, 19, 12, 31]
l1 = [1, 19]
l2 = [5, 9]
l3 = [3, 31]
l4 = [15, 25]
l5 = [1, 17]
lst = [l1, l2, l3, l4, l5]
lst = selection_sort(lst, key=lambda l: l[0], key2=lambda l: l[1], reverse=False, reverse2=True)
print(lst)
print('--------------------------')
lst = [l1, l2, l3, l4, l5]
lst = selectionsort(lst)
print(lst)
