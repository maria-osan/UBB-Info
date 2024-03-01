from domain.entities import Imobil


class ImobilService:
    def __init__(self, imobil_repo, imobil_val):
        """
        Initializare valori
        :type imobil_repo: ImobilFileRepo
        :type imobil_val: ValidateImobil
        """
        self.__validare_imobil = imobil_val
        self.__repo_imobil = imobil_repo

    def get_all_imobile(self):
        """
        Returneaza lista cu toate imobilele
        :return: lista de imobile
        :rtype: list of Imobil objects
        """
        return self.__repo_imobil.get_all_imobile()

    def find_imobil(self, id_imobil):
        """
        Cauta imobilul cu ID-ul dat
        :param id_imobil: ID-ul dat
        :type id_imobil: int
        :return: imobilul daca se gaseste, None altfel
        :rtype: Imobil
        """
        return self.__repo_imobil.find_imobil(id_imobil)

    def medie_pret(self, tip_oferta):
        """
        Calculeaza media pe pret_dorit pentru un tip de oferta dat
        :param tip_oferta: tipul de oferta
        :type tip_oferta: str
        :return: media calculata
        :rtype: float
        """
        all_imobile = self.get_all_imobile()
        suma = 0
        cate_imobile = 0
        for imobil in all_imobile:
            if imobil.get_tip() == tip_oferta:
                suma = suma + imobil.get_pret()
                cate_imobile = cate_imobile + 1

        if cate_imobile > 0:
            medie = suma / cate_imobile
            return medie
        else:
            return -1

    def test_find_imobil(self):
        imobil1 = Imobil(23, 'str. Cernei nr. 10 Cluj-Napoca', 60000, 'vanzare')

        imobil = self.find_imobil(23)
        assert (imobil.get_pret() == imobil1.get_pret())
        assert (imobil.get_adresa() == imobil1.get_adresa())
        assert (imobil.get_tip() == imobil1.get_tip())

        imobil = self.find_imobil(200)
        assert (imobil is None)

    def test_medie_pret(self):
        assert (self.medie_pret('inchiriere') == -1)
