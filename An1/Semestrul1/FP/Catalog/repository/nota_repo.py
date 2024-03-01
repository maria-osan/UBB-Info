from domain.entities import Student, Disciplina, Nota


class InMemoryRepositoryNota:
    def __init__(self):
        self.__note = []

    def find_nota(self, n):
        """
        Cauta nota in lista de note
        :param n: nota cautata
        :type n: Nota
        :return: nota cautata daca exista in lista, None altfel
        :rtype: Nota
        """
        for nota in self.__note:
            if n == nota:
                return nota
        return None

    def store_nota(self, nota):
        """
        Adauga o nota
        :param nota: nota de adaugat
        :type nota: Nota
        :return: -; se adauga nota la lista de note
        """
        self.__note.append(nota)

    def get_all_note(self):
        """
        Returneaza o lista cu toate notele disponibile
        :return: lista cu note
        :rtype: list of Nota objects
        """
        return self.__note


class NotaFileRepo:
    def __init__(self, filename):
        self.__filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Incarca datele din fisier
        :return: lista de note din fisier
        :rtype: list of Nota object
        """
        try:
            f = open(self.__filename, 'r')
        except IOError:
            return

        lines = f.readlines()
        all_note = []
        for line in lines:
            stud_nume, stud_id, dis_nume, dis_id, dis_profesor, nota_acordata = [token.strip() for token in line.split(';')]
            # stud_id = int(stud_id)
            #dis_id = int(dis_id)
            nota_acordata = float(nota_acordata)

            stud = Student(stud_nume, stud_id)
            dis = Disciplina(dis_nume, dis_id, dis_profesor)
            nota = Nota(stud, dis, nota_acordata)
            all_note.append(nota)

        f.close()
        return all_note

    def __save_to_file(self, all_note):
        """
        Salveaza notele in fisier
        """
        with open(self.__filename, 'w') as f:
            for nota in all_note:
                nota_string = str(nota.getStudent().getNume()) + ';' + str(nota.getStudent().getIDStudent) + ';' + \
                              str(nota.getDisciplina().getNume) + ';' + str(nota.getDisciplina().getIDDisciplina) + \
                              ';' + str(nota.getDisciplina().getProfesor()) + ';' + str(nota.getNota()) + '\n'
                f.write(nota_string)

    def find_nota(self, n):
        """
        Cauta nota in lista de note
        :param n: nota cautata
        :type n: Nota
        :return: nota cautata daca exista in lista, None altfel
        :rtype: Nota
        """
        all_note = self.__load_from_file()
        for nota in all_note:
            if n == nota:
                return nota
        return None

    def store_nota(self, nota):
        """
        Adauga o nota
        :param nota: nota de adaugat
        :type nota: Nota
        :return: -; se adauga nota la lista de note
        """
        all_note = self.__load_from_file()

        all_note.append(nota)
        self.__save_to_file(all_note)

    def get_all_note(self):
        """
        Returneaza o losta cu tote notele
        :rtype: list of objects de tip Nota
        """
        return self.__load_from_file()

    def size(self):
        """
        Returneaza numarul de note
        :return: numar note existente in lista
        :rtype: int
        """
        return len(self.__load_from_file())

    def delete_all(self):
        self.__save_to_file([])

    def get_studentsNote(self, dis):
        """
        Returneaza lista cu toti studentii si notele pe care le au la o disciplina data
        :param dis: disciplina data
        :type: Disciplina
        :return: lista de studenti
        """
        list_note = self.__load_from_file()
        stud_note = []
        for nota in list_note:
            if nota.getDisciplina().getIDDisciplina() == dis.getIDDisciplina():
                stud = nota.getStudent()
                # print(stud)
                lst = [stud, nota.getNota()]
                stud_note.append(lst)
        return stud_note

    def medie(self, list_stud):
        """
        Returneaza lista cu media notelor fiecarui student
        :return: lista de medii
        """
        list_note = self.__load_from_file()
        medie = []
        for stud in list_stud:
            suma = 0
            cate = 0
            for nota in list_note:
                # print(nota.getStudent().getIDStudent(), stud.getIDStudent())
                if nota.getStudent().getIDStudent() == stud.getIDStudent():
                    # print(nota)
                    suma = suma + nota.getNota()
                    cate = cate + 1
            if cate != 0:
                medie = suma / cate
                lst = [stud, medie]
                medie.append(lst)
        return medie

    def get_top_3(self, dis, list_stud):
        """
        Returneaza lista cu media notelor fiecarui student
        :param dis: sidciplina data
        :type dis: Disciplina
        :param list_stud: lista de studenti
        :type list_stud: list of Student object
        :return: lista de medii
        :rtype: list of MedieNote objects
        """
        list_note = self.__load_from_file()
        medie = []
        for stud in list_stud:
            suma = 0
            cate = 0
            for nota in list_note:
                if stud == nota.getStudent() and nota.getDisciplina() == dis:
                    cate = cate + 1
                    suma = suma + nota.getNota()
            if cate != 0:
                medie = suma / cate
                lst = [medie, stud]
                medie.append(lst)
        return medie


def test_store_nota():
    stud = Student('Ema Pop', 1236)
    dis = Disciplina('Matematica', 5629, 'Dana Rosca')

    nota = Nota(stud, dis, 3.8)

    test_repo = InMemoryRepositoryNota()
    test_repo.store_nota(nota)

    assert(len(test_repo.get_all_note()) == 1)


# test_store_nota()
