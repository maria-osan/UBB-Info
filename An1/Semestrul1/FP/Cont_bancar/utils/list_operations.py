def print_list(lst):
    for i in lst:
        for el in i:
            print('Zi:', el[0], '- Suma:', el[1], '- Tip:', el[2])


def add_tranzactie(lst, s):
    """
    Adauga o tranzactie noua in lista:
    :param lst: lista de tranzactii
    :type lst: list
    :param s: tranzactia care trebuie adaugata
    :type s: list
    :return: modifica lista (list)
    """
    lst.append(s)


def afisare_sum(lst, s):
    """
    Afiseaza tranzactiile care au suma mai mare decat o suma data
    :param lst: lista de tranzactii
    :type lst: list
    :param s: suma data
    :type s: int, s>=0
    """
    for i in lst:
        if i[1]>s:
            print('Zi:', i[0], '- Suma:', i[1], '- Tip:', i[2])


def afisare_zi_sum(lst, z, s):
    """
    Afiseaza tranzactiile efectuate inainte de o zi si care au suma mai mare decat o suma data
    :param lst: lista de tranzactii
    :type lst: list
    :param z: ziua data
    :type z: int, z>0 && z<=31
    :param s: suma data
    :type s: int, s>=0
    """
    for i in lst:
        if i[0]<z and i[1]>s:
            print('Zi:', i[0], '- Suma:', i[1], '- Tip:', i[2])



def afisare_tip(lst, t):
    """
    Afiseaza tranzactiile care sunt de un anumit tip
    :param lst: lista de tranzactii
    :type lst: list
    :param t: tipul dat
    :type t: int, t==1 || t==2
    """
    for i in lst:
        if i[2]==t:
            print('Zi:', i[0], '- Suma:', i[1], '- Tip:', i[2])


def make_list_copy(lst):
    """
    Face o copie la o lista de liste
    :param lst: lista care se copiaza
    :type lst: list (of lists)
    :return: copie a listei date
    :rtype: list (of lists)
    """
    cpy=[]
    for el in lst:
        cpy.append(el)
    return cpy
