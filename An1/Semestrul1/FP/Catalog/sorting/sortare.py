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


def selection_sort(lista, *, key=lambda x: x, reverse=False):
    """
    Implementarea algoritmului de sortare Selection sort
    :param lista: lista
    :param key: functie dupa care se face sortarea
    :param reverse: metoda dupa care se face storarea (True - crescator, False - descrescator)
    :return list: lista sortata
    """
    for i in range(0, len(lista) - 1):
        ind = i
        if reverse is False:   # sortare crescatoare
            # cauta cel mai mic element din restul listei
            for j in range(i + 1, len(lista)):
                if key(lista[j]) < key(lista[ind]):
                    ind = j
            if i < ind:
                # interschimbare elemente
                swap(lista, i, ind)

        elif reverse is True:   # sortare descrescatoare
            # cauta cel mai mare element din restul listei
            for j in range(i + 1, len(lista)):
                if key(lista[j]) > key(lista[ind]):
                    ind = j
            if i < ind:
                # interschimbare elemente
                swap(lista, i, ind)
    return lista


def shake_sort(lista, *, key=lambda x: x, reverse=False):
    """
    Implementarea algoritmului de sortare Shake sort
    :param lista: lista
    :param key: functie dupa care se face sortarea
    :param reverse: metoda dupa care se face storarea (cresc, descresc)
    :return: lista sortata

    Complexitate:
    - timp de executie: complexitatea la cazul defavorabil/mediu este la fel: O(n^2), iar la cazul favorabil este O(n);
    - spatiu de memorie: Shake Sort este un algoritm In-place: memoria aditionala este O(1).
    """
    for i in range(len(lista) - 1, 0, -1):
        is_swapped = False

        if reverse is False:
            for j in range(i, 0, -1):
                if key(lista[j]) < key(lista[j - 1]):
                    swap(lista, j, j - 1)
                    is_swapped = True

            for j in range(i):
                if key(lista[j]) > key(lista[j + 1]):
                    swap(lista, j, j + 1)
                    is_swapped = True

        if reverse is True:
            for j in range(i, 0, -1):
                if key(lista[j]) > key(lista[j - 1]):
                    swap(lista, j, j - 1)
                    is_swapped = True

            for j in range(i):
                if key(lista[j]) < key(lista[j + 1]):
                    swap(lista, j, j + 1)
                    is_swapped = True

        if not is_swapped:
            return lista


def selectionsort(lista, *, key=lambda x: x, key2=lambda x: x, reverse=False, reverse2=False):
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
