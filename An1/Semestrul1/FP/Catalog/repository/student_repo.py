from domain.entities import Student
from exceptions.exceptions import DuplicateIDException, StudentNotFoundException


class InMemoryRepositoryStudent:
    def __init__(self):
        # students - multimea de studenti pe care o gestionam
        self.__students = []

    def find_student(self, id_student):
        """
        Cauta studentul cu id-ul dat
        :param id_student: id-ul dat
        :type id_student: int
        :return: studentul cu id-ul dat, None daca nu exista
        :rtype: Student
        """
        for stud in self.__students:
            if stud.getIDStudent() == id_student:
                return stud
        return None

    def search_student(self, id_student):
        """
        Cauta studentul cu id-ul dat
        :param id_student: id-ul dat
        :type id_student: int
        :return: studentul cautat
        :rtype: Student
        :raises: ValueError daca nu exista student cu id-ul dat
        """
        stud = self.find_student(id_student)
        if stud is None:
            raise ValueError('Nu exista student cu acest id.')
        return stud

    def store_student(self, stud):
        """
        Adauga un student in lista
        :param stud: studentul pe care il adaugam
        :type stud: Student
        :return: -; lista de studenti se modifica prin adaugarea studentului dat
        """
        if self.find_student(stud.getIDStudent()) is not None:
            raise ValueError('Exisat deja studentul cu acest id.')
        self.__students.append(stud)

    def get_all_students(self):
        """
        Returneaza o lista cu toti studentii
        :rtype: list of objects de tip Student
        """
        return self.__students

    def size(self):
        """
        Returneaza numarul de studenti
        :return: numar studenti
        :rtype: int
        """
        return len(self.__students)

    def update(self, id_student, modified_stud):
        """
        Modifica datele studentului cu id-ul dat
        :param id_student: id-ul studentului dat
        :type id_student: int
        :param modified_stud: studentul cu date noi
        :type modified_stud: Student
        :return: studentul modificat
        :rtype: Student
        """
        stud = self.find_student(id_student)
        if stud is None:
            raise ValueError('Nu exista student cu acest id.')
        stud.setNume(modified_stud.getNume())
        return stud

    def delete_student(self, id_student):
        """
        Sterge studentul cu un id dat din lista de studenti
        :param id_student: id-ul studentului dat
        :type id_student: int (>0)
        :return: studentul sters
        :rtype: Student
        :raises: ValueError daca id-ul nu exista
        """
        stud = self.find_student(id_student)
        if stud is None:
            raise ValueError('Nu exista student cu acest id.')
        self.__students.remove(stud)
        return stud


def test_store_student():
    test_repo = InMemoryRepositoryStudent()
    stud1 = Student('Ema Pop', 1236)
    test_repo.store_student(stud1)
    assert (test_repo.size() == 1)

    stud2 = Student('Ana Hagau', 2015)
    test_repo.store_student(stud2)
    assert (test_repo.size() == 2)

    try:
        test_repo.store_student(stud2)
        assert False
    except ValueError:
        assert True


def setup_test_repo():
    stud1 = Student('Ema Pop', 1236)
    stud2 = Student('Ana Hagau', 2015)
    stud3 = Student('Nadia Maxim', 1547)
    stud4 = Student('Alex Baciu', 473)
    stud5 = Student('Florin Coroiu', 908)

    test_repo = InMemoryRepositoryStudent()
    test_repo.store_student(stud1)
    test_repo.store_student(stud2)
    test_repo.store_student(stud3)
    test_repo.store_student(stud4)
    test_repo.store_student(stud5)
    return test_repo


def test_find_student():
    test_repo = setup_test_repo()

    p = test_repo.find_student(2015)
    assert (p.getNume() == 'Ana Hagau')

    p1 = test_repo.find_student(2016)
    assert (p1 is None)


def test_size():
    test_repo = setup_test_repo()
    assert (test_repo.size() == 5)

    test_repo.delete_student(473)
    test_repo.delete_student(1547)
    assert (test_repo.size() == 3)

    test_repo.store_student(Student('Denisa Coroiu', 251))
    assert (test_repo.size() == 4)

    test_repo.update(908, Student('Florin Muntean', 908))
    assert (test_repo.size() == 4)


def test_get_all():
    test_repo = setup_test_repo()
    ctr_stud = test_repo.get_all_students()
    assert (type(ctr_stud) == list)
    assert (len(ctr_stud) == 5)

    test_repo.delete_student(473)
    test_repo.delete_student(1547)
    ctr_stud = test_repo.get_all_students()
    assert (len(ctr_stud) == 3)

    test_repo.store_student(Student('Denisa Coroiu', 251))
    ctr_stud = test_repo.get_all_students()
    assert (len(ctr_stud) == 4)


def test_update():
    test_repo = setup_test_repo()
    stud = Student('Florin Muntean', 908)
    modified_stud = test_repo.update(908, stud)
    assert (modified_stud.getNume() == 'Florin Muntean')

    try:
        test_repo.update(1234, Student('Florin Muntean', 908))
        assert False
    except ValueError:
        assert True


def test_delete():
    test_repo = setup_test_repo()
    delete_stud = test_repo.delete_student(1236)
    assert (delete_stud.getNume() == 'Ema Pop')
    assert (test_repo.size() == 4)

    try:
        test_repo.delete_student(2022)
        assert False
    except ValueError:
        assert True


test_store_student()
test_find_student()
test_size()
test_get_all()
test_update()
test_delete()


class StudentFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de studenti din fisier
        :rtype: list of Student object
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        all_stud = []

        for line in f:
            stud_nume = str(line)
            line = next(f)
            stud_id = str(line)

            stud_nume = stud_nume.replace('\n', '')
            stud_id = int(stud_id)
            stud = Student(stud_nume, stud_id)
            all_stud.append(stud)

        # lines = f.readlines()
        # for line in lines:
        #    stud_nume, stud_id = [token.strip() for token in line.split(';')]
        #    stud_id = int(stud_id)
        #    stud = Student(stud_nume, stud_id)
        #    all_stud.append(stud)

        f.close()
        return all_stud

    def __save_to_file(self, all_stud):
        """
        Salveaza studentii in fisier
        """
        with open(self.__filename, 'w') as f:
            for stud in all_stud:
                # stud_string = str(str(stud.getNume()) + ';' + str(stud.getIDStudent()) + '\n')
                # f.write(stud_string)
                f.write(str(stud.getNume()))
                f.write('\n')
                f.write(str(stud.getIDStudent()))
                f.write('\n')

    def find_student(self, id_stud):
        """
        Cauta studentul cu id-ul dat
        :param id_stud: id-ul dat
        :type id_stud: int
        :return: studentul cu id-ul dat, None daca nu exista
        :rtype: Student
        """
        all_stud = self.__load_from_file()
        for stud in all_stud:
            if stud.getIDStudent() == id_stud:
                return stud
        return None

    def search_stud_recursiv(self, id_stud, all_stud):
        """
        Cauta studentul cu id-ul dat recursiv
        :param id_stud: id-ul dat
        :type id_stud: int
        :param all_stud: lista de studenti
        :type all_stud: list of Student Object
        :return: studentul cautat
        :rtype: Student
        """
        if not all_stud:
            raise None
        if all_stud[0].getIDStudent() == id_stud:
            return all_stud[0]
        return self.search_stud_recursiv(id_stud, all_stud[1:])

    def store_student(self, stud):
        """
        Adauga un student in lista
        :param stud: studentul care se adauga
        :type stud: Student
        :return: -; lista de studenti se modifica prin adaugarea studentului dat
        :raises: DuplicateIDException daca studentul exista deja in lista
        """
        all_stud = self.__load_from_file()
        # if stud in all_stud:
            # raise DuplicateIDException()

        all_stud.append(stud)
        self.__save_to_file(all_stud)

    def get_all_students(self):
        """
        Returneaza o losta cu toti studentii
        :rtype: list of objects de tip Student
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de studenti
        :return: numar studenti existenti in lista
        :rtype: int
        """
        return len(self.__load_from_file())

    def find_index(self, all_stud, id_stud):
        """
        Gaseste pozitia in lista a studentului cu id-ul dat
        :param all_stud: lista cu toti studentii
        :type all_stud: list od Student objects
        :param id_stud: id-ul cautat
        :type id_stud: int
        :return: pozitia in lista a studentului cu id-ul dat, -1 daca studentul nu se regasetet in lista
        :rtype: int, >=0, <repo.size()
        """
        index = -1
        for i in range(len(all_stud)):
            if all_stud[i].getIDStudent() == id_stud:
                index = i
        return index

    def delete_student(self, id_stud):
        """
        Sterge studentul dupa id
        :param id_stud: id-ul dat
        :type id_stud: int
        :return: studentul sters
        :rtype: Student
        :raises: StudentNotFoundException daca id-ul nu exista
        """
        all_stud = self.__load_from_file()
        index = self.find_index(all_stud, id_stud)
        if index == -1:
            # raise StudentNotFoundException
            raise ValueError

        deleted_stud = all_stud.pop(index)

        self.__save_to_file(all_stud)
        return deleted_stud

    def update(self, id_stud, modified_stud):
        """
        Modifica datele studentului cu id-ul dat
        :param id_stud: id-ul dat
        :type id_stud: int
        :param modified_stud: studentul cu datele noi
        :type modified_stud: Student
        :return: studentul modificat
        :rtype: Student
        :raises: ValoeError daca nu exista studentul cu id-ul dat
        """
        all_stud = self.__load_from_file()
        index = self.find_index(all_stud, id_stud)
        if index == -1:
            raise ValueError('Studentul cu id-ul dat nu a fost gasit.')

        all_stud[index] = modified_stud

        self.__save_to_file(all_stud)
        return modified_stud

    def delete_all(self):
        self.__save_to_file([])
