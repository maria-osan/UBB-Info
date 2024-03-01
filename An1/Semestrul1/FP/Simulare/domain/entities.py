class Imobil:
    def __init__(self, id_imobil, adresa, pret_dorit, tip_oferta):
        """
        Initializare date
        :param id_imobil: ID-ul imobilului
        :type id_imobil: int
        :param adresa: adresa la care se afla imobilul
        :type adresa: str
        :param pret_dorit: pretul dorit pe imobil
        :type pret_dorit: int
        :param tip_oferta: tipul de oferta al imobilului
        :type tip_oferta: str
        """
        self.__id_imobil = id_imobil
        self.__adresa = adresa
        self.__pret_dorit = pret_dorit
        self.__tip_oferta = tip_oferta

    def get_id(self):
        return self.__id_imobil

    def get_adresa(self):
        return self.__adresa

    def get_pret(self):
        return self.__pret_dorit

    def get_tip(self):
        return self.__tip_oferta

    def set_id(self, val):
        self.__id_imobil = val

    def set_adresa(self, val):
        self.__adresa = val

    def set_pret(self, val):
        self.__pret_dorit = val

    def set_tip(self, val):
        self.__tip_oferta = val
