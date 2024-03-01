from domain.entities import Student
from domain.validators import StudentValidator
# from repository.student_repo import InMemoryRepositoryStudent
from repository.student_repo import StudentFileRepo
from sorting.sortare import selection_sort, shake_sort
import random


class StudentService:
    def __init__(self, repo_stud, validator):
        """
        Initializeaza service
        :param repo_stud: obiect de tip repo care ne ajuta sa gestionam multimea studentilor
        :type repo_stud: InMemoryRepositoryStudent
        :param validator: validator pentru verificare
        :type validator: CatalogValidator
        """
        self.__repo_stud = repo_stud
        self.__validator_stud = validator

    def add_student(self, nume, id_student):
        """
        Adauga student
        :param nume: numele elevului
        :type nume: str
        :param id_student: id-ul studentului
        :type id_student:int
        :return: obiectul de tip Student creat
        :rtype:-; studentul s-a adaugat in lista
        :raises: ValueError daca studentul are date invalide
        """
        stud = Student(nume, id_student)
        # self.__validator_stud.validate_stud(stud)
        self.__repo_stud.store_student(stud)
        return stud

    def get_all_students(self):
        """
        Returneaza o lista cu toti studentii
        :return: lista de studenti
        :rtype: list of objects de tip Student
        """
        return self.__repo_stud.get_all_students()

    def delete_student(self, id_student):
        """
        Sterge studentul cu un id dat din lista de studenti
        :param id_student: id-ul studentului dat
        :type id_student: int (>0)
        :rtype: list of objects de tip Student
        """
        return self.__repo_stud.delete_student(id_student)

    def update_student(self, id_student, nume):
        """
        Modifica datele studentului cu id-ul dat
        :param id_student: id-ul studentului de modificat
        :type id_student: int
        :param nume: noul nume al studentului
        :type nume: str
        :return: studentul modificat
        :rtype: Student
        :raises: ValueError daca noile date nu sunt valide, sau nu exista student cu id-ul dat
        """
        stud = Student(nume, id_student)
        # self.__validator_stud.validate_stud(stud)
        return self.__repo_stud.update(id_student, stud)

    def search_student(self, id_student):
        """
        Cauta studentul cu id-ul dat
        :param id_student: id-ul dat
        :type id_student: int
        :return: studentul cautat
        :rtype: Student
        :raises: ValueError daca nu exista student cu id-ul dat
        """
        if self.__repo_stud.find_student(id_student) is None:
            raise ValueError('Nu exista dstudent cu acest id.')
        return self.__repo_stud.find_student(id_student)

    def search_student_recursiv(self, id_stud, all_stud):
        """
        Cauta studentul cu id-ul dat recursiv
        :param id_stud: id-ul dat
        :type id_stud: int
        :param all_stud: lista de studenti
        :type all_stud: list of Student object
        :return: studentul cautat
        :rtype: Student
        :raises: ValueError daca nu exista student cu id-ul dat
        """
        if self.__repo_stud.find_student(id_stud) is None:
            raise ValueError('Nu exista dstudent cu acest id.')
        return self.__repo_stud.search_stud_recursiv(id_stud, all_stud)

    def selection_sotred(self):
        """
        Sorteaza lista de studenti dupa ID
        :return: lista sortata
        """
        list_stud = self.__repo_stud.get_all_students()
        list_stud = selection_sort(list_stud, key=lambda l: l.getIDStudent(), reverse=False)
        return list_stud

    def sortare_shake(self):
        """
        Sorteaza lista de studenti alfabetic
        :return: lista sortata
        """
        list_stud = self.__repo_stud.get_all_students()
        list_stud = shake_sort(list_stud, key=lambda l: l.getNume(), reverse=False)
        return list_stud

    # def generate(self):
    #     stud1 = Student('Ema Pop', 1236)
    #     stud2 = Student('Ana Hagau', 2015)
    #     stud3 = Student('Nadia Maxim', 1547)
    #     stud4 = Student('Alex Baciu', 473)
    #     stud5 = Student('Florin Coroiu', 908)
    #
    #     self.__repo_stud.store_student(stud1)
    #     self.__repo_stud.store_student(stud2)
    #     self.__repo_stud.store_student(stud3)
    #     self.__repo_stud.store_student(stud4)
    #     self.__repo_stud.store_student(stud5)

    def generate_random(self):
        id_student = random.randint(0, 10000)
        nume = chr(random.randint(ord('a'), ord('z')))
        for i in range(1, random.randint(1, 9)):
            nume += chr(random.randint(ord('a'), ord('z')))
        stud = Student(nume, id_student)
        return stud

    def generate_list(self):
        for i in range(10):
            stud = self.generate_random()
            self.__repo_stud.store_student(stud)


def test_add_student():
    # repo = InMemoryRepositoryStudent()
    repo = StudentFileRepo('student.txt')
    validator = StudentValidator()
    test_srv = StudentService(repo, validator)

    added_stud = test_srv.add_student('Ema Pop', 1236)
    assert (added_stud.getNume() == 'Ema Pop')
    assert (added_stud.getIDStudent() == 1236)

    assert (len(test_srv.get_all_students()) == 1)


# test_add_student()
