from domain.entities import Client


class ClientService:
    def __init__(self, val_client, repo_client):
        self.__validator_client = val_client
        self.__repo_client = repo_client

    def add_client(self, nume, id_client, cnp_client):
        """
        Adauga un client nou in lista
        :param nume: numele clientului
        :type nume: str
        :param id_client: ID-ul clientului
        :type id_client: int
        :param cnp_client: CNP-ul clientului
        :type cnp_client: int
        :return: studentul adaugat
        :rtype: Client
        :raises: ValueError daca datele tastate sunt invalide
        """
        client = Client(nume, id_client, cnp_client)
        self.__validator_client.validate_client(client)
        self.__repo_client.store_client(client)
        return client

    def get_all_clients(self):
        """
        :return: Returneaza lista cu toti clientii
        :rtype: list od Client objects
        """
        return self.__repo_client.get_all_clients()

    def delete_client(self, id_client):
        """
        Sterge clientul cu id-ul dat din lista
        :param id_client: id-ul dat
        :type id_client: int
        :return:
        """
        return self.__repo_client.delete_client(id_client)

    def update_client(self, id_client, nume, cnp_client):
        """
        Modifica datele clientului cu ID-ul dat
        :param id_client: ID-ul clientului
        :type id_client: int
        :param nume: numele clientului
        :type nume: str
        :param cnp_client: CNP-ul clientului
        :type cnp_client: int
        :return: clientul cu datele modificate
        """
        modified_client = Client(nume, id_client, cnp_client)
        self.__validator_client.validate_client(modified_client)
        return self.__repo_client.update_client(id_client, modified_client)

    def search_client(self, id_client):
        """
        Cauta clientul cu ID-ul dat in lista de clienti
        :param id_client: ID-ul clientului
        :type id_client: int
        :return: clientul cautat
        :rtype: Client
        """
        return self.__repo_client.find_client(id_client)

    def ordonare_clients(self):
        """
        Ordoneaza lista de clienti in ordine alfabetica
        """
        all_clients = self.get_all_clients()
        new_clients_list = sorted(all_clients, key=lambda client: client.get_nume(), reverse=False)
        return new_clients_list

# teste
