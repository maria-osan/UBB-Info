from domain.entities import Disciplina
from domain.validators import DisciplinaValidator
# from repository.disciplina_repo import InMemoryRepositoryDisciplina
from repository.disciplina_repo import DisciplinaFileRepo


class DisciplinaService:
    def __init__(self, repo_dis, validator):
        """
        Initializare service
        :param repo_dis: obiect de tip repo care ne ajuta sa gestionam multimea disciplinelor
        :type repo_dis: InMemoryRepository
        :param validator: validator pentru verificare
        :type validator: CatalogValidator
        """
        self.__repo_dis = repo_dis
        self.__validator_dis = validator

    def add_disciplina(self, nume, id_disciplina, profesor):
        """
        Adauga disciplina
        :param nume: numele disciplinei
        :type nume: str
        :param id_disciplina: id-ul disciplinei
        :type id_disciplina: int
        :param profesor: numele profesorului care preda disciplina
        :type profesor: str
        :return: obiectul de tip Disciplina creat
        :rtype:-; disciplina s-a adaugat in lista
        :raises: ValueError daca disciplina are date invalide
        """
        dis = Disciplina(nume, id_disciplina, profesor)
        # self.__validator_dis.validate_dis(dis)
        self.__repo_dis.store_disciplina(dis)
        return dis

    def get_all_discipline(self):
        """
        Returneaza o lista cu toate disciplinele
        :return: lista de discipline
        :rtype: list of objects de tip Disciplina
        """
        return self.__repo_dis.get_all_discipline()

    def delete_disciplina(self, id_disciplina):
        """
        Sterge disciplina cu un id dat din lista de discipline
        :param id_disciplina: id-ul disciplinei date
        :type id_disciplina: int (>0)
        :rtype: list of objects de tip Disciplina
        """
        return self.__repo_dis.delete_disciplina(id_disciplina)

    def update_disciplina(self, id_disciplina, nume, profesor):
        """
        Modifica datele disciplinei cu id-ul dat
        :param id_disciplina: id-ul disciplinei de modificat
        :type id_disciplina: int
        :param nume: noul nume al disciplinei
        :type nume: str
        :param profesor: noul nume al profesorului
        :type profesor: str
        :return: disciplina modificata
        :rtype: Disciplina
        :raises: ValueError daca noile date nu sunt valide, sau nu exista disciplina cu id-ul dat
        """
        dis = Disciplina(nume, id_disciplina, profesor)
        # self.__validator_dis.validate_dis(dis)
        return self.__repo_dis.update(id_disciplina, dis)

    def search_disciplina(self, id_disciplina):
        """
        Cauta disciplina cu id-ul dat
        :param id_disciplina: id-ul dat
        :type id_disciplina: int
        :return: disciplina cautata
        :rtype: Disciplina
        :raises: ValueError daca nu exista disciplina cu id-ul dat
        """
        if self.__repo_dis.find_disciplina(id_disciplina) is None:
            raise ValueError('Nu exista disciplina cu acest id.')
        return self.__repo_dis.find_disciplina(id_disciplina)

    # def generate(self):
    #    dis1 = Disciplina('Matematica', 5, 'Dana Morar')
    #    dis2 = Disciplina('Desen', 8762, 'Delia Bodor')
    #    dis3 = Disciplina('Romana', 5629, 'Anca Morari')

    #    self.__repo_dis.store_disciplina(dis1)
    #    self.__repo_dis.store_disciplina(dis2)
    #    self.__repo_dis.store_disciplina(dis3)


def test_add_disciplina():
    # repo = InMemoryRepositoryDisciplina()
    repo = DisciplinaFileRepo('discipline.txt')
    validator = DisciplinaValidator()
    test_srv = DisciplinaService(repo, validator)

    added_dis = test_srv.add_disciplina('Desen', 8762, 'Delia Bodor')
    assert (added_dis.getNume() == 'Desen')
    assert (added_dis.getIDDisciplina() == 8762)
    assert (added_dis.getProfesor() == 'Delia Bodor')

    assert (len(test_srv.get_all_discipline()) == 1)


# test_add_disciplina()
