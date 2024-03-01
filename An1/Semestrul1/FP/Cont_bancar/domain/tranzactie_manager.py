from domain.tranzactie import get_sum, validate_tranzactie
from utils.list_operations import make_list_copy,add_tranzactie


def generate_tranzactii():
    """
    Genereaza o lista de tranzactii
    :param l: lista de tranzactii
    :type l: list
    :param si: tranzactia care se adauga in lista
    :type si: list
    :return: lista de tranzactii generata
    """
    s1=[25, 456, 1]
    s2=[23, 56, 2]
    s3=[17, 283, 2]
    s4=[4, 619, 1]
    s5=[5, 300, 1]
    s6=[30, 172, 2]
    l=[s1, s2, s3, s4, s5, s6]
    return l


def setup_tranzactii_manager(add_predefined):
    """
    Initializeaza un obiect de tip tranzactie manager
    :param add_predefined: indicator pentru adaugarea serialelor predefinite in lista curenta de seriale
            daca add_predefined==True se incepe cu o lista populata de seriale predefinite, altfel cu o lista
            goala de seriale
    :type add_predefined: bool
    :return: o lista cu 2 pozitii care reprezinta tranzactie_manager-ul, tranzactie_manager[0] - lista curenta de tranzactii
            tranzactie_manager[1] - undo_list
    :rtype: list
    """
    if add_predefined:
        lst=generate_tranzactii()
    else:
        lst=[]

    undo_list=[]
    return [lst, undo_list]


# getters
def get_tranzactie_list(tranzactie_manager):
    return tranzactie_manager[0]

def get_undo_list(tranzactie_manager):
    return tranzactie_manager[1]


# setters
def set_tranzactie_list(tranzactie_manager, new_lst):
    tranzactie_manager[0]=new_lst

def set_undo_list(tranzactie_manager, new_undo_list):
    tranzactie_manager[1]=new_undo_list


def add_tranzactie_to_manager(tranzactie_manager, lst):
    """
    :param tranzactie_manager: obiect de tip tranzactie manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :param lst: lista care va fi adaugata
    :type lst: list
    :return: se modifica lista curenta de tranzactii prin adaugarea celei noi
    :raises ValueError daca serialul pentru care se incearca adaugarea este invalid
    """
    validate_tranzactie(lst)

    crt_list=get_tranzactie_list(tranzactie_manager)
    undo_list=get_undo_list(tranzactie_manager)

    undo_list.append(make_list_copy(crt_list))

    add_tranzactie(get_tranzactie_list(tranzactie_manager), lst)


def delete_tranzactie_from_manager_zi(tranzactie_manager, zi):
    """
    Sterge tranzactii din lista dintr-o zi specificata
    :param tranzactie_manager: obiect de tip show manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :param zi: ziua specificata
    :type zi: int
    :return: se modifica lista curenta de tranzactii prin stergerea acestora
    """
    crt_list=get_tranzactie_list(tranzactie_manager)
    undo_list=get_undo_list(tranzactie_manager)

    undo_list.append(make_list_copy(crt_list))

    set_tranzactie_list(tranzactie_manager, delete_tranzactii_zi(crt_list, zi))


def delete_tranzactie_from_manager_perioada(tranzactie_manager, zi_start, zi_end):
    """
    Sterge tranzactii din lista dintr-o perioada data
    :param tranzactie_manager: obiect de tip show manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :param zi_start: ziua sde inceput
    :type zi_start: int
    :param zi_end: ziua de sfarsit
    :type zi_end: int
    :return: se modifica lista curenta de tranzactii prin stergerea acestora
    """
    crt_list=get_tranzactie_list(tranzactie_manager)
    undo_list=get_undo_list(tranzactie_manager)

    undo_list.append(make_list_copy(crt_list))

    set_tranzactie_list(tranzactie_manager, delete_tranzactii_perioada(crt_list, zi_start, zi_end))


def delete_tranzactie_from_manager_sum(tranzactie_manager, suma):
    """
    Sterge tranzactii din lista dintr-o zi specificata
    :param tranzactie_manager: obiect de tip show manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :param suma: suma data
    :type suma: int
    :return: se modifica lista curenta de tranzactii prin stergerea acestora
    """
    crt_list=get_tranzactie_list(tranzactie_manager)
    undo_list=get_undo_list(tranzactie_manager)

    undo_list.append(make_list_copy(crt_list))

    set_tranzactie_list(tranzactie_manager, delete_tranzactii_sum(crt_list, suma))


def delete_tranzactie_from_manager_tip(tranzactie_manager, tip):
    """
    Sterge tranzactii din lista care au un anumit tip
    :param tranzactie_manager: obiect de tip show manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :param tip: tipul specificat
    :type tip: int
    :return: se modifica lista curenta de tranzactii prin stergerea acestora
    """
    crt_list=get_tranzactie_list(tranzactie_manager)
    undo_list=get_undo_list(tranzactie_manager)

    undo_list.append(make_list_copy(crt_list))

    set_tranzactie_list(tranzactie_manager, delete_tranzactii_tip(crt_list, tip))


def undo(tranzactie_manager):
    """
    Face undo la ultima operatie de adaugare sau stergere
     :param tranzactie_manager: obiect de tip tranzactie manager
    :type tranzactie_manager: list (len(tranzactie_manager)=2, tranzactie_manager[0] = lista crt de tranzactii,
        tranzactie_manager[1] = lista de undo
    :return: lista curenta de tranzactii revine la starea de dinainte de ultima operatie
    """
    undo_list = get_undo_list(tranzactie_manager)

    if len(undo_list)==0:
        raise ValueError("Nu se mai poate face undo.")
    else:
        previous_list=undo_list[-1]

        set_tranzactie_list(tranzactie_manager, previous_list)
        set_undo_list(tranzactie_manager, undo_list[:-1])


def get_sum_tip(l, t):
    """
    Determina suma totala a tranzactiilor de un anumit tip
    :param l: lista de tranzactii
    :type l: list
    :param t: tipul dat
    :type t: int, t==1 (intrare) || t==2 (iesire)
    """
    s = 0
    for i in l:
        if i[2]==t:
            s=s+i[1]
    return s


def get_sum_tip_zi(l, t, z):
    """
    Determina suma totala a tranzactiilor de un anumit tip si cu ziua mai mica sau egala decat o zi specificata
    :param l: lista de tranzactii
    :type l: list
    :param t: tipul dat
    :type t: int, t==1 (intrare) || t==2 (iesire)
    :param z: ziua data
    :type z: int, z>0 && z<=31
    """
    s = 0
    for i in l:
        if i[2]==t and i[0]<=z:
            s=s+i[1]
    return s


def delete_tranzactii_tip(l, t):
    """
    Sterge din lista de tranzactii toate tranzactiile de un anumit tip
    :param l: lista de tranzactii
    :type l: list
    :param t: tipul de tranzactie
    :type t: int, t==1 (intrare) || t==2 (iesire)
    :return: lista de tranzactii fara tranzactiile de tipul t
    """
    new_list=[s for s in l if s[2] != t]
    return new_list


def delete_tranzactii_sum(l, s):
    """
    Sterge din lista de tranzactii toate tranzactiile cu suma mai mica decat o suma data
    :param l: lista de tranzactii
    :type l: list
    :param s: suma data
    :type s: int, s>=0
    :return: lista de tranzactii fara tranzactiile cu suma mai mica decat o suma data
    """
    new_list=[i for i in l if i[1] > s]
    return new_list


def delete_tranzactii_zi(l, z):
    """
    Sterge din lista de tranzactii toate tranzactiile care au data = cu ziua specificata de utilizator
    :param l: lista de tranzactii
    :type l: list
    :param z: data specificata
    :type z: int, z>=1 && z<=31
    :return: lista de tranzactii fara tranzactiile din ziua data
    """
    new_list=[i for i in l if i[0] != z]
    return new_list


def delete_tranzactii_perioada(l, zi, zf):
    """
    Stergere toate tranzacțiile dintr-o perioada data (se da ziua de inceput si sfarsit)
    :param l: lista de tranzactii
    :type l: list
    :param zi: ziua de inceput
    :type zi: int
    :param zf: ziua de sfarsit
    :type zf: int
    :return: returneaza o noua lista (list)
    """
    #for i in range(len(l)):
        #if (get_zi(l[i])>=zi and get_zi(l[i])<=zf):
            #del l[i]
    #return l
    new_list=[i for i in l if i[0] < zi or i[0] > zf]
    return new_list


def ordonare_lista(l):
    """
    Ordoneaza lista de tranzactii dupa suma
    :param l: lista de tranzactii
    :type l: list
    """
    l.sort(key=get_sum)
    return l


def test_ordonare_lista():
    l=generate_tranzactii()
    l=ordonare_lista(l)
    assert (l[0][1]==56)
    assert (l[1][1]==283)
    assert (l[2][1]==456)
    assert (l[3][1]==619)

def test_get_sum_tip():
    l=generate_tranzactii()
    assert (get_sum_tip(l, 1)==1075)
    assert (get_sum_tip(l, 2)==339)

def test_get_sum_tip_zi():
    l=generate_tranzactii()
    assert (get_sum_tip_zi(l, 1, 23)==619)
    assert (get_sum_tip_zi(l, 2, 23)==339)

def test_delete_tranzactii_tip():
    l=generate_tranzactii()
    s=[11, 137, 1]
    l.append(s)
    l=delete_tranzactii_tip(l, 2)
    assert (len(l)==3)

def test_delete_tranzactii_sum():
    l=generate_tranzactii()
    l=delete_tranzactii_sum(l, 300)
    assert (len(l)==2)

def test_delete_tranzactii_zi():
    l=generate_tranzactii()
    l=delete_tranzactii_zi(l, 23)
    assert (len(l)==3)

def test_delete_tranzactii_perioada():
    l=generate_tranzactii()
    l=delete_tranzactii_perioada(l, 20, 30)
    assert (len(l)==2)
