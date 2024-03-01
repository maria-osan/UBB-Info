from domain.entities import Disciplina
from exceptions.exceptions import DisciplinaNotFoundException


class InMemoryRepositoryDisciplina:
    def __init__(self):
        # discipline - multimea de discipline pe care o gestionam
        # self.__discipline = []
        self.__discipline = {}

    def find_disciplina(self, id_disciplina):
        """
        Cauta disciplina cu id-ul dat
        :param id_disciplina: id-ul disciplinei date
        :type id_disciplina: int
        :return: disciplina cu id-ul dat, None daca nu exista disciplina cu id-ul dat
        :rtype: Disciplina
        """
        if id_disciplina in self.__discipline:
            return self.__discipline[id_disciplina]
        return None

    def search_disciplina(self, id_disciplina):
        """
        Cauta disciplina cu id-ul dat
        :param id_disciplina: id-ul dat
        :type id_disciplina: int
        :return: disciplina cautata
        :rtype: Disciplina
        :raises: ValueError daca nu exista disciplina cu id-ul dat
        """
        if id_disciplina not in self.__discipline:
            raise ValueError('Nu exista disciplina cu acest id.')
        return self.__discipline[id_disciplina]

    def store_disciplina(self, dis):
        """
        Adauga o disciplina in lista
        :param dis: disciplina pe care o adaugam
        :type dis: Disciplina
        :return: -; lista de discipline se modifica prin adaugarea disciplinei date
        """
        # if self.find_disciplina(dis.getIDDisciplina()) is not None:
        #     raise ValueError('Exisat deja disciplina cu acest id.')
        # self.__discipline.append(dis)
        if dis.getIDDisciplina() in self.__discipline:
            raise ValueError('Exisat deja disciplina cu acest id.')
        self.__discipline[dis.getIDDisciplina()] = dis

    def get_all_discipline(self):
        """
        Returneaza o lista cu toate disciplinele
        :rtype: list of objects de tip Disciplina
        """
        return self.__discipline

    def size(self):
        """
        Returneaza numarul de discipline
        :return: numarul disciplinelor existente
        :rtype: int
        """
        return len(self.__discipline)

    def update(self, id_disciplina, modified_dis):
        """
        Modifica datele disciplinei cu id-ul dat
        :param id_disciplina: id-ul dat
        :type id_disciplina: int
        :param modified_dis: disciplina cu datele noi
        :type modified_dis: Disciplina
        :return: disciplina modificata
        :rtype: Disciplina
        """
        if id_disciplina not in self.__discipline:
            raise ValueError('Nu exista disciplina cu acest id.')
        self.__discipline[id_disciplina] = modified_dis
        return modified_dis

    def delete_disciplina(self, id_disciplina):
        """
        Sterge disciplina cu un id dat din lista de discipline
        :param id_disciplina: id-ul dat
        :type id_disciplina: int (>0)
        :return: disciplina stearsa
        :rtype: Disciplina
        :raises: ValueError daca id-ul nu exista
        """
        # dis = self.__discipline
        # if dis is None:
        #     raise ValueError('Nu exista disciplina cu acest id.')
        # self.__discipline.remove(dis)
        # return dis
        if id_disciplina not in self.__discipline:
            raise ValueError('Nu exista disciplina cu acest id.')
        deleted_dis = self.__discipline[id_disciplina]
        del self.__discipline[id_disciplina]
        return deleted_dis


class DisciplinaFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de discipline din fisier
        :rtype: list of Disciplina object
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        all_dis = {}
        for line in lines:
            dis_nume, dis_id, dis_profesor = [token.strip() for token in line.split(';')]
            dis_id = int(dis_id)
            dis = Disciplina(dis_nume, dis_id, dis_profesor)
            all_dis[dis_id] = dis

        f.close()
        return all_dis

    def __save_to_file(self, all_dis):
        """
        Salveaza disciplinele in fisier
        """
        print(all_dis)
        with open(self.__filename, 'w') as f:
            for dis in all_dis:
                dis_string = str(all_dis[dis].getNume()) + ';' + str(all_dis[dis].getIDDisciplina()) + ';' \
                             + str(all_dis[dis].getProfesor()) + '\n'
                f.write(dis_string)

    def find_disciplina(self, id_dis):
        """
        Cauta disciplina cu id-ul dat
        :param id_dis: id-ul dat
        :type id_dis: int
        :return: disciplina cu id-ul dat, None daca nu exista
        :rtype: Disciplina
        """
        all_dis = self.__load_from_file()
        if id_dis in all_dis:
            return all_dis[id_dis]
        return None

    def store_disciplina(self, dis):
        """
        Adauga o disciplina in lista
        :param dis: disciplina care se adauga
        :type dis: Disciplina
        :return: -; lista de discipline se modifica prin adaugarea studentului dat
        :raise: DuplicateIDException daca disciplina exista deja in lista
        """
        all_dis = self.__load_from_file()
        # if dis in all_dis:
            # raise DuplicateIDException

        all_dis[dis.getIDDisciplina()] = dis
        self.__save_to_file(all_dis)

    def get_all_discipline(self):
        """
        Returneaza o losta cu toate disciplinele
        :rtype: list of objects de tip Disciplina
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de discipline
        :return: numar disciplinelor existente in lista
        :rtype: int
        """
        return len(self.__load_from_file())

    def delete_disciplina(self, id_dis):
        """
        Sterge disciplina dupa id
        :param id_dis: id-ul disciplinei
        :type id_dis: int
        :return: disciplina stearsa
        :rtype: Disciplina
        :raises: DisciplinaNotFoundException daca id-ul nu exista
        """
        all_dis = self.__load_from_file()
        if id_dis not in all_dis:
            raise DisciplinaNotFoundException

        deleted_dis = all_dis.pop(id_dis)

        self.__save_to_file(all_dis)
        return deleted_dis

    def update(self, id_dis, modified_dis):
        """
        Modifica datele disciplinei cu id-ul dat
        :param id_dis: id-ul dat
        :type id_dis: int
        :param modified_dis: disciplina cu datele noi
        :type modified_dis: Disciplina
        :return: disciplina modificata
        :rtype: Disciplina
        :raises: ValueError daca nu exista disciplina cu id-ul dat
        """
        all_dis = self.__load_from_file()
        if id_dis not in all_dis:
            raise ValueError('Disciplina cu id-ul dat nu exista.')

        all_dis[id_dis] = modified_dis

        self.__save_to_file(all_dis)
        return modified_dis

    def delete_all(self):
        self.__save_to_file({})
