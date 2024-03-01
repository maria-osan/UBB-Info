class Console:
    def __init__(self, srv_client, srv_movie):
        """
        Initializare consola
        :param srv_client: ClientService
        :param srv_movie: MovieService
        """
        self.__srv_client = srv_client
        self.__srv_movie = srv_movie

    def __print_meniu(self):
        print('Comenzi disponibile pentru client: add, delete, update, search, show_all, ordonare, exit.')

    def __print_all_clients(self):
        """
        Afiseaza toti clientii
        """
        clients_list = self.__srv_client.get_all_clients()
        if len(clients_list) == 0:
            print('Nu exista clienti in lista.')
        else:
            print('Lista de clienti este:')
            for client in clients_list:
                print('Nume client: ', client.get_nume(), ' - ID client: ', str(client.get_id()), ' - CNP client: ', str(client.get_cnp()))

    def __add_client(self):
        """
        Adauga un client cu datele citite de la tastatura
        """
        nume = input('Dati numele: ')
        try:
            id_client = int(input('Dati ID-ul:'))
            cnp_client = int(input('Dati CNP-ul: '))
        except ValueError:
            print('ID-ul clientului trebuie sa fie un numar pozitiv iar CNP-ul trebuie sa contina exact 13 cifre.')
            return

        try:
            added_client = self.__srv_client.add_client(nume, id_client, cnp_client)
            print('Clientul: ' + added_client.get_nume() + ' a fost adaugat cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __delete_client(self):
        """
        Sterge un clientul cu ID-ul dat
        """
        try:
            id_client = int(input('Dati ID-ul: '))
        except ValueError:
            print('ID-ul clientului trebuie sa fie un numar pozitiv.')

        try:
            deleted_client = self.__srv_client.delete_client(id_client)
            return deleted_client
        except ValueError as ve:
            print(str(ve))
            return

    def __update_client(self):
        """
        Modifica un client cu ID-ul dat
        """
        try:
            id_client = int(input('Dati ID-ul: '))
        except ValueError:
            print('ID-ul clientului trebuie sa fie un numar pozitiv.')
            return

        try:
            nume = input('Dati numele: ')
        except ValueError:
            print('Numeletrebuie sa contina minim 2 caractere.')
            return

        try:
            cnp_client = input('Dati CNP-ul: ')
        except ValueError:
            print('CNP-ul trebuie sa contina minim 13 caractere.')
            return

        try:
            modified_client = self.__srv_client.update_client(id_client, nume, cnp_client)
            print('Clientul: ' + str(modified_client.get_id()) + ' - ' + str(modified_client.get_nume()) + ' a fost modificat cu succes.')
        except ValueError as ve:
            print((str(ve)))
            return

    def __search_client(self):
        try:
            id_client = int(input('Dati ID-ul: '))
        except ValueError:
            print('ID-ul clientului trebuie sa fie un numar pozitiv.')
            return

        try:
            client = self.__srv_client.search_client(id_client)
            if client is None:
                raise ValueError('Nu exista client cu ID-ul dat.')
            else:
                print('Clientul cautat este: ' + str(client.get_id()) + ' - ' + str(client.get_nume()) + ' - ' + str(client.get_cnp()))
        except ValueError as ve:
            print(str(ve))
            return

    def __ordonare_clients(self):
        """
        Ordoneaza lista de clienti in ordine alfabetica
        """
        try:
            clients_list = self.__srv_client.ordonare_clients()
            for client in clients_list:
                print('ID: ' + str(client.get_id()) + ' - Nume:' + str(client.get_nume()) + ' - CNP:' + str(client.get_cnp()))
        except ValueError as ve:
            print(str(ve))
            return

    def inchiriere_ui(self):
        while True:
            self.__print_meniu()
            cmd = input('Comanda este:')
            cmd = cmd.lower().strip()
            if cmd == 'add':
                self.__add_client()
            elif cmd == 'delete':
                self.__delete_client()
            elif cmd == 'update':
                self.__update_client()
            elif cmd == 'search':
                self.__search_client()
            elif cmd == 'show_all':
                self.__print_all_clients()
            elif cmd == 'ordonare':
                self.__ordonare_clients()
            elif cmd == 'exit':
                return
            else:
                print('Comanda invalida.')

