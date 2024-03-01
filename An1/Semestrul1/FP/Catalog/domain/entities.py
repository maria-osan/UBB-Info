class Student:
    def __init__(self, nume, id_student):
        """
        :param nume: numele studentului
        :type nume: str
        :param id_student: id-ul studentului
        :type id_student: int (>0)
        """
        self.__nume = nume
        self.__id_student = id_student

    def getNume(self):
        return self.__nume

    def getIDStudent(self):
        return self.__id_student

    def setNume(self, value):
        self.__nume = value

    def setIDStudent(self, value):
        self.__id_student = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre studentul curent si studentul other
        :param other:
        :type other: Student
        :return: True daca studentii sunt egali (=au acelasi nume si acelasi id), False altfel
        :rtype: bool
        """
        if self.__id_student == other.getIDStudent():
            return True
        return False

    def __str__(self):
        return "Nume student: " + self.__nume + '; ID student: ' + str(self.__id_student)


class Disciplina:
    def __init__(self, nume, id_disciplina, profesor):
        """
        :param nume: numele disciplinei
        :type nume: str
        :param id_disciplina: id-ul disciplinei
        :type id_disciplina: int (>0)
        :param profesor: numele profesorului care preda disciplina
        :type profesor: str
        """
        self.__nume = nume
        self.__id_disciplina = id_disciplina
        self.__profesor = profesor

    def getNume(self):
        return self.__nume

    def getIDDisciplina(self):
        return self.__id_disciplina

    def getProfesor(self):
        return self.__profesor

    def setNume(self, value):
        self.__nume = value

    def setIDDisciplina(self, value):
        self.__id_disciplina = value

    def setProfesor(self, value):
        self.__profesor = value

    def __eq__(self, other):
        """
        Verifica egalitatea intre disciplina curenta si disciplina other
        :param other:
        :type other: Disciplina
        :return: True daca disciplinele sunt egale (=au acelasi nume si acelasi id), False altfel
        :rtype: bool
        """
        if self.__id_disciplina == other.getIDDisciplina():
            return True
        return False

    def __str__(self):
        return "Nume disciplina: " + self.__nume + '; ID disciplina: ' + str(self.__id_disciplina) + '; Profesor: ' + \
               self.__profesor


class Nota:
    def __init__(self, student, disciplina, nota):
        """
        :param student: studentul dat
        :type student: Student
        :param disciplina: disciplina data
        :type disciplina: Disciplina
        :param nota: nota acordata studentului dat la disciplina data
        :type nota: float
        """
        self.__student = student
        self.__disciplina = disciplina
        self.__nota = nota

    def getStudent(self):
        return self.__student

    def getDisciplina(self):
        return self.__disciplina

    def getNota(self):
        return self.__nota

    def setStudent(self, value):
        self.__student = value

    def setDisciplina(self, value):
        self.__disciplina = value

    def setNota(self, value):
        self.__nota = value

    def __str__(self):
        return 'Student: [' + str(self.__student.getIDStudent()) + '; ' + str(self.__student.getNume()) + '] ' + \
               'Disciplina: [' + str(self.__disciplina.getIDDisciplina()) + '; ' + self.__disciplina.getNume() + '; ' +\
                str(self.__disciplina.getProfesor()) + '] ' + 'Nota: ' + str(self.__nota)


def test_create_student():
    stud1 = Student('Ema Pop', 1236)
    assert (stud1.getNume() == 'Ema Pop')
    assert (stud1.getIDStudent() == 1236)

    stud1.setNume('Vasile Pastor')
    stud1.setIDStudent(8762)

    assert (stud1.getNume() == 'Vasile Pastor')
    assert (stud1.getIDStudent() == 8762)


def test_equals_student():
    stud1 = Student('Ana Hagau', 2015)
    stud2 = Student('Ana Hagau', 2015)

    assert (stud1 == stud2)

    stud3 = Student('Nadia Maxim', 1547)
    assert (stud1 != stud3)


def test_create_disciplina():
    dis1 = Disciplina('Matematica', 5629, 'Dana Rosca')
    assert (dis1.getNume() == 'Matematica')
    assert (dis1.getIDDisciplina() == 5629)
    assert (dis1.getProfesor() == 'Dana Rosca')

    dis1.setNume('Desen')
    dis1.setIDDisciplina(8762)
    dis1.setProfesor('Delia Bodor')

    assert (dis1.getNume() == 'Desen')
    assert (dis1.getIDDisciplina() == 8762)
    assert (dis1.getProfesor() == 'Delia Bodor')


def test_equals_disciplina():
    dis1 = Disciplina('Matematica', 5629, 'Dana Rosca')
    dis2 = Disciplina('Matematica', 5629, 'Dana Rosca')

    assert (dis1 == dis2)

    dis3 = Disciplina('Desen', 8762, 'Delia Bodor')
    assert (dis1 != dis3)


def test_create_nota():
    stud = Student('Ema Pop', 1236)
    dis = Disciplina('Matematica', 5629, 'Dana Rosca')

    nota = Nota(stud, dis, 8.75)

    assert (nota.getStudent() == stud)
    assert (nota.getDisciplina() == dis)
    assert (nota.getNota() == 8.75)


# test_create_student()
# test_equals_student()

# test_create_disciplina()
# test_equals_disciplina()

# test_create_nota()
