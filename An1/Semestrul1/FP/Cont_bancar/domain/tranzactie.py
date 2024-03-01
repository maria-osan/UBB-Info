def create_tranzactie(zi, suma, tip):
    """
    Creeaza o tranzactie
    :param zi: ziua tranzactiei
    :type zi: int
    :param suma: suma tranzactiei
    :type suma: int
    :param tip: tipul tranzactiei
    :type tip: int
    :return: tranzactia creata
    :rtype: list [zi, suma, tip]
    """
    return [zi, suma, tip]


def actualizare_tranzactie(tranzactie_manager):
    """
    Modifica o tranzactie in lista:
    """
    ok=0
    zi=int(input("Ziua tranzactiei:"))
    for lst in tranzactie_manager:
        for i in lst:
            if i[0]==zi:
                suma=int(input("Suma tranzactiei:"))
                tip=int(input("Tipul tranzactiei (intrare - 1 sau iesire - 2):"))
                i[1]=suma
                i[2]=tip
                print("Tranzactia s-a actualizat cu succes.")
                ok=1
    if ok==0:
        print('Ziua introdusa nu se gaseste in lista de tranzactii')


def validate_tranzactie(lst):
    """
    Verifica daca uo tranzactie este valida
    :param lst: tranzactia
    :type lst: list
    :raises: ValueError daca serialul dat este invalid
    """
    errors=[]
    if get_zi(lst)<1 or get_zi(lst)>31:
        errors.append('Valoarea introdusa pentru ziua tranzactiei este invalida.')
    if get_sum(lst)<0:
        errors.append('Suma tranzactiei trebuie sa fie mai mare de 0.')
    if get_tip(lst)!=1 and get_tip(lst)!=2:
        errors.append('Tipul tranzactiei trebuie sa fie 1 (intrare) sau 2 (iesire).')

    if len(errors)>0:
        errors_string='\n'.join(errors)
        raise ValueError(errors_string)


# getters

def get_zi(l):
    return l[0]

def get_sum(l):
    return l[1]

def get_tip(l):
    return l[2]


# setters

def set_zi(l, z):
    l[0] = z

def set_sum(l, s):
    l[1] = s

def set_tip(l, t):
    l[2] = t


def test_create_tranzactie():
    lst1=create_tranzactie(5, 30, 2)
    assert (type(lst1)==list)
    assert (get_zi(lst1)==5)
    assert (get_sum(lst1)==30)
    assert (get_tip(lst1)==2)


def test_validate_tranzactie():
    lst1=create_tranzactie(53, 30, 2)
    try:
        validate_tranzactie(lst1)
        assert False
    except ValueError as ve:
        assert(str(ve)=='Valoarea introdusa pentru ziua tranzactiei este invalida.')

    lst2=create_tranzactie(5, -30, 2)
    try:
        validate_tranzactie(lst2)
        assert False
    except ValueError as ve:
        assert(str(ve)=='Suma tranzactiei trebuie sa fie mai mare de 0.')

    lst3=create_tranzactie(5, 30, 7)
    try:
        validate_tranzactie(lst3)
        assert False
    except ValueError as ve:
        assert(str(ve)=='Tipul tranzactiei trebuie sa fie 1 (intrare) sau 2 (iesire).')

    lst4=create_tranzactie(53, -30, 2)
    try:
        validate_tranzactie(lst4)
        assert False
    except ValueError as ve:
        assert(str(ve)=='Valoarea introdusa pentru ziua tranzactiei este invalida.\nSuma tranzactiei trebuie sa fie mai'
                        ' mare de 0.')