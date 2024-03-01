from domain.entities import Imobil


class ImobilFileRepo:
    def __init__(self, filename):
        """
        Initializare date
        :param filename: numele fisierului
        """
        self.__filename = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        all_imobile = []
        lines = f.readlines()
        for line in lines:
            id_imobil, adresa, pret_dorit, tip_oferta = [token.strip() for token in line.split(',')]
            id_imobil = int(id_imobil)
            pret_dorit = int(pret_dorit)
            imobil = Imobil(id_imobil, adresa, pret_dorit, tip_oferta)
            all_imobile.append(imobil)

        f.close()
        return all_imobile

    def __save_to_file(self, all_imobile):
        """
        Salveaza datele in fisies
        """
        with open(self.__filename, 'w') as f:
            for imobil in all_imobile:
                string_imobil = (str(imobil.get_id()) + ',' + str(imobil.get_adresa()) + ',' + str(imobil.get_pret()) + ',' + str(imobil.get_tip()))
                f.write(string_imobil)

    def find_imobil(self, id_imobil):
        """
        Cauta imobilul cu ID-ul dat
        :param id_imobil: ID-ul dat
        :type id_imobil: int
        :return: imobilul daca se gaseste, None altfel
        :rtype: Imobil
        """
        all_imobile = self.__load_from_file()
        for imobil in all_imobile:
            if imobil.get_id() == id_imobil:
                return imobil
        return None

    def get_all_imobile(self):
        """
        Returneaza lista cu toate imobilele
        :return: lista de imobile
        :rtype: list of Imobil objects
        """
        return self.__load_from_file()
