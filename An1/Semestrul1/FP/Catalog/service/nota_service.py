from domain.entities import Nota
from exceptions.exceptions import StudentNotFoundException, DisciplinaNotFoundException
from sorting.sortare import shake_sort, selectionsort


class NotaService:
    def __init__(self, nota_repo, validator, stud_repo, dis_repo):
        self.__nota_repo = nota_repo
        self.__validator_nota = validator
        self.__stud_repo = stud_repo
        self.__dis_repo = dis_repo

    def create_nota(self, stud_id, dis_id, nota_acordata):
        """
        Creeaza o nota
        :param stud_id: id-ul studentului evaluat
        :type stud_id: int
        :param dis_id: id-ul disciplinei la care este evaluat
        :type dis_id: int
        :param nota_acordata: nota acordata studentului (1-10)
        :type nota_acordata: float
        :return: nota creata cu datele date
        :rtype: Nota
        :raises: StudentNotFoundException
                 DisciplinaNotFoundException
                 ValidationException
        """
        stud = self.__stud_repo.find_student(stud_id)
        if stud is None:
            raise StudentNotFoundException()

        dis = self.__dis_repo.find_disciplina(dis_id)
        if dis is None:
            raise DisciplinaNotFoundException()

        nota = Nota(stud, dis, nota_acordata)
        # self.__validator_nota.validate_nota(nota)
        self.__nota_repo.store_nota(nota)
        return nota

    def adaugare_nota(self, nota):
        self.__nota_repo.store_nota(nota)

    def get_all_note(self):
        return self.__nota_repo.get_all_note()

    def ordonare(self, dis):
        """
        Ordoneaza studentii in functie de notele de la o disciplina data, alfabetic
        :param dis: disciplina
        :return: lista ordonata
        """
        stud_note = self.__nota_repo.get_studentsNote(dis)
        print(stud_note)
        new_stud_note = sorted(stud_note, key=lambda l: (l[0].getNume(), l[1]), reverse=False)
        return new_stud_note

    def medie(self, list_stud):
        medie_note = self.__nota_repo.medie(list_stud)
        new_medie_note = sorted(medie_note, key=lambda l: l[1], reverse=True)
        size = self.__nota_repo.size()
        size = int(size/5)
        new_medie_note = new_medie_note[:size]
        return new_medie_note

    def top_3(self, list_stud):
        """
        Determina primii 3 studenti in functie de medie
        :param list_stud: lista de studenti
        :return: lista cu primii 3 studenti in functie de medie
        """
        top_3 = self.__nota_repo.medie(list_stud)
        new_top_3 = sorted(top_3, key=lambda l: l[0], reverse=True)
        new_top_3 = new_top_3[:3]
        return new_top_3

    def sortare_shake(self):
        """
        Sorteaza lista de note
        :return: lista sortata
        """
        list_note = self.__nota_repo.get_all_note()
        list_note = shake_sort(list_note, key=lambda l: l.getNota(), reverse=True)
        return list_note

    def selectionsort(self):
        """
        Sorteaza lista de note dupa 2 criterii: alfabetic si dupa note
        :return: lista sortata
        """
        list_note = self.__nota_repo.get_all_note()
        list_note = selectionsort(list_note, key=lambda l: l.getStudent().getNume(), key2=lambda l: l.getNota(), reverse=False, reverse2=True)
        return list_note

    # def generate(self):
    #    nota1 = Nota(Student('Ema Pop', 1236), Disciplina('Matematica', 5, 'Dana Morar'), 8.75)
    #    nota2 = Nota(Student('Ema Pop', 1236), Disciplina('Matematica', 5, 'Dana Morar'), 9.05)
    #    nota3 = Nota(Student('Ema Pop', 1236), Disciplina('Romana', 5629, 'Anca Morari'), 9.85)
    #    nota4 = Nota(Student('Ana Hagau', 2015), Disciplina('Desen', 8762, 'Delia Bodor'), 10)
    #    nota5 = Nota(Student('Ana Hagau', 2015), Disciplina('Matematica', 5, 'Dana Morar'), 5.45)
    #    nota6 = Nota(Student('Nadia Maxim', 1547), Disciplina('Romana', 5629, 'Anca Morari'), 7.25)
    #    nota7 = Nota(Student('Alex Baciu', 473), Disciplina('Matematica', 5, 'Dana Morar'), 6.85)
    #    nota8 = Nota(Student('Alex Baciu', 473), Disciplina('Romana', 5629, 'Anca Morari'), 6.90)
    #    nota9 = Nota(Student('Alex Baciu', 473), Disciplina('Romana', 5629, 'Anca Morari'), 9.65)
    #    nota10 = Nota(Student('Alex Baciu', 473), Disciplina('Desen', 8762, 'Delia Bodor'), 9.90)
    #    nota11 = Nota(Student('Florin Coroiu', 908), Disciplina('Matematica', 5, 'Dana Morar'), 8.75)
    #    nota12 = Nota(Student('Florin Coroiu', 908), Disciplina('Romana', 5629, 'Anca Morari'), 9.95)

    #    self.__nota_repo.store_nota(nota1)
    #    self.__nota_repo.store_nota(nota2)
    #    self.__nota_repo.store_nota(nota3)
    #    self.__nota_repo.store_nota(nota4)
    #    self.__nota_repo.store_nota(nota5)
    #    self.__nota_repo.store_nota(nota6)
    #    self.__nota_repo.store_nota(nota7)
    #    self.__nota_repo.store_nota(nota8)
    #    self.__nota_repo.store_nota(nota9)
    #    self.__nota_repo.store_nota(nota10)
    #    self.__nota_repo.store_nota(nota11)
    #    self.__nota_repo.store_nota(nota12)
