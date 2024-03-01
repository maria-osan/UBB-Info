class Console:
    def __init__(self, imobil_service):
        """
        Initializare date
        :type imobil_service: ImobilService
        """
        self.__srv_imobil = imobil_service

    def __print_meniu(self):
        """
        Tipareste meniul
        """
        print('Meniul este: media, efectuare_tranzactie, exit')

    def __media_pret(self):
        """
        Determina media pe pret_dorit pentru un tip de oferta
        """
        try:
            tip_oferta = input('Dati tipul ofertei: ')
        except ValueError as ve:
            print('Tipul de oferta poate fi vanzare sau inchiriere.')
            return

        try:
            medie_pret = self.__srv_imobil.medie_pret(tip_oferta)
            if medie_pret >= 0:
                print('Media pe pret pentru tipul ', tip_oferta, ' este: ', medie_pret, '.')
            else:
                print('Nu se poate calcula media deoarece nu se gasesc imobile cu tipul de oferta dorit.')
                return
        except ValueError as ve:
            print(str(ve))
            return

    def __efectuare_tranzactie(self):
        """
        Efectueaza o tranzactie pentru un imobil cu un ID dat si pretul negociat pe acesta
        """
        try:
            id_imobil = int(input('Dati ID-ul: '))
            pret_negociat = float(input('Dati pretul: '))
        except ValueError as ve:
            print(str(ve))
            return

        try:
            imobil = self.__srv_imobil.find_imobil(id_imobil)
            if imobil is None:
                print('Nu exista imobil cu ID-ul introdus.')
                return
            else:
                if imobil.get_tip() == 'vanzare':
                    comision = 2/100*pret_negociat
                elif imobil.get_tip() == 'inchiriere':
                    comision = 5/10*pret_negociat
                print('Adresa imobilului cu ID-ul: ', id_imobil, ' este: ', str(imobil.get_adresa()), ' si comisionul aferent tranzactiei este de: ', comision, '.')
        except ValueError as ve:
            print(str(ve))
            return

    def agentie_imobiliara(self):
        while True:
            self.teste()
            self.__print_meniu()
            cmd = input('Dati comanda: ')
            cmd = cmd.lower().strip()
            if cmd == 'media':
                self.__media_pret()
            elif cmd == 'efectuare_tranzactie':
                self.__efectuare_tranzactie()
            elif cmd == 'exit':
                return
            else:
                print('Comanda invalida.')

    def teste(self):
        self.__srv_imobil.test_find_imobil()
        self.__srv_imobil.test_medie_pret()
