class Client:
    def __init__(self, nume, id_client, cnp):
        """
        :param nume: numele clientului
        :type nume: str
        :param id_client: id-ul clientului
        :type id_client: int
        :param cnp: CNP-ul clientului
        :type cnp: int
        """
        self.__nume = nume
        self.__id_client = id_client
        self.__cnp = cnp

    def get_nume(self):
        return self.__nume

    def get_id(self):
        return self.__id_client

    def get_cnp(self):
        return self.__cnp

    def set_nume(self, val):
        self.__nume = val

    def set_id(self, val):
        self.__id_client = val

    def set_cnp(self, val):
        self.__cnp = val

    def __str__(self):
        return 'Nume client: ' + self.__nume + ' - Id client: ' + str(self.__id_client) + ' - CNP client: ' + str(self.__cnp)

    def __eq__(self, other):
        """
        Verifica egalitatea dintre clientul self si clientul other
        :type other: Client
        :return: True daca clientii sunt egali (=au acelasi cnp si acelasi id), False altfel
        :rtype: bool
        """
        if self.__id_client == other.get_id() and self.__cnp == other.get_cnp():
            return True
        return False


class Movie:
    def __init__(self, id_movie, titlu, descriere, gen):
        """
        :param id_movie: ID-ul filmului
        :type id_movie: int
        :param titlu: titlul filmului
        :type titlu: str
        :param descriere: descrierea filmului
        :type descriere: str
        :param gen: genul filumuli
        :type gen: str
        """
        self.__id_movie = id_movie
        self.__titlu = titlu
        self.__descriere = descriere
        self.__gen = gen

    def get_id(self):
        return self.__id_movie

    def get_titlu(self):
        return self.__titlu

    def get_descriere(self):
        return self.__descriere

    def get_gen(self):
        return self.__gen

    def set_id(self, val):
        self.__id_movie = val

    def set_titlu(self, val):
        self.__titlu = val

    def set_descriere(self, val):
        self.__descriere = val

    def set_gen(self, val):
        self.__gen = val

# teste
