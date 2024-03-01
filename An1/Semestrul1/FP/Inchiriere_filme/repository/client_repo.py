from domain.entities import Client


class ClientFileRepo:
    def __init__(self, filemane):
        self.__filemane = filemane

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de clienti din fisier
        :rtype: list of Client objects
        """
        try:
            f = open(self.__filemane, 'r')
        except IOError:
            return

        all_clients = []
        lines = f.readlines()
        for line in lines:
            client_nume, client_id, clinet_cnp = [token.strip() for token in line.split(';')]
            client_id = int(client_id)
            clinet_cnp = int(clinet_cnp)
            client = Client(client_nume, client_id, clinet_cnp)
            all_clients.append(client)

        f.close()
        return all_clients

    def __save_to_file(self, all_clients):
        """
        Salveaza datele in fisier
        :param all_clients: lista cu clienti
        :type all_clients: list of Client object
        """
        with open(self.__filemane, 'w') as f:
            for client in all_clients:
                client_string = str(client.get_nume()) + ';' + str(client.get_id()) + ';' + str(client.get_cnp()) + '\n'
                f.write(client_string)

    def find_client(self, id_client):
        """
        Cauta clientul cu id-ul dat
        :param id_client: id-ul clientului
        :type id_client: int
        :return: clientul cu id-ul dat, None daca nu exista
        """
        all_clients = self.__load_from_file()
        for client in all_clients:
            if client.get_id() == id_client:
                return client
        return None

    def store_client(self, client):
        """
        Adauga un client in lista
        :param client: clientul care se adauga
        :type client: Client
        :return: -; lista de clienti de modifica prin adaugarea clientului dat
        :raises: ValueError daca exista deja clientul in lista
        """
        # if self.find_client(client.get_id()) is not None:
            # raise ValueError('Clietul cu acest id exista deja in lista.')

        all_clients = self.__load_from_file()
        if client in all_clients:
            raise ValueError('Clietul cu acest id exista deja in lista.')
        all_clients.append(client)
        self.__save_to_file(all_clients)

    def get_all_clients(self):
        """
        :return: Returneaza o linta cu toti clientii
        :rtype: list of Client objects
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de clienti
        :return: numarul clientilor
        :rtype: int
        """
        return len(self.__load_from_file())

    def find_index(self, all_clients, id_client):
        """
        Gaseste pozitia in lista a clientului cu id-ul dat
        :param all_clients: lista de clienti
        :type all_clients: list of Client objects
        :param id_client: id-ul dat
        :type id_client: int
        :return: pozitia in lista a clientului cu id-ul dat, -1 daca clientul nu se regaseste in lista
        """
        index = -1
        for i in range(len(all_clients)):
            if all_clients[i].get_id() == id_client:
                index = i
        return index

    def delete_client(self, id_client):
        """
        Sterge clientul cu ID-ul dat din lista
        :param id_client: ID-ul clientului
        :type id_client: int
        :return: clientul sters
        :rtype: Client
        :raises: ValueError daca clientul cu ID-ul dat nu exista
        """
        all_clients = self.__load_from_file()
        index = self.find_index(all_clients, id_client)
        if index == -1:
            raise ValueError('Nu exista client cu id-ul dat.')
        delete_client = all_clients.pop(index)
        self.__save_to_file(all_clients)
        return delete_client

    def update_client(self, id_client, modified_client):
        """
        Modifica datele unui client cu ID-ul dat
        :param id_client: ID-ul dat
        :type id_client: int
        :param modified_client: clientul cu datele de modificat
        :type modified_client: Client
        :return: clientul cu datele modificate
        :rtype: Client
        :raises: ValueError daca clientul cu ID-ul dat nu exista
        """
        all_clients = self.__load_from_file()
        index = self.find_index(all_clients, id_client)
        if index == -1:
            raise ValueError('Nu exista client cu id-ul dat.')
        all_clients[index] = modified_client
        self.__save_to_file(all_clients)
        return modified_client

# teste
