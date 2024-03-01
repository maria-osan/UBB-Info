class Console:
    def __init__(self, srv_stud, srv_dis, srv_nota):
        """
        Initializeaza consola
        :type srv_stud: StudentService
        :type srv_dis: DisciplinaService
        :type srv_nota: NotaService
        """
        self.__srv_stud = srv_stud
        self.__srv_dis = srv_dis
        self.__srv_nota = srv_nota

    def __print_menu(self):
        print('--- MENIU ---')
        print('Student: ')
        print('11. Adauga')
        print('12. Sterge')
        print('13. Modifica')
        print('14. Cauta')
        print('15. Afisare')
        print('Disciplina: ')
        print('21. Adauga')
        print('22. Sterge')
        print('23. Modifica')
        print('24. Cauta')
        print('25. Afisare')
        print('Nota: ')
        print('31. Adauga')
        print('32. Afisare')
        print('33. Ordonare')
        print('34. Top 20% dupa medie')
        print('35. Top 3')
        print('Sortari: ')
        print('1. Selection sort')
        print('2. Shake sort')
        print('3. Sortare dupa 2 criterii')
        print('\nx. Exit')

    def __print_all_students(self):
        """
        Afiseaza toti studentii
        """
        stud_list = self.__srv_stud.get_all_students()
        if len(stud_list) == 0:
            print('Nu exista studenti in lista.')
        else:
            print('Lista de studenti este:')
            for stud in stud_list:
                print('Nume student: ', stud.getNume(), ' - Id student: ', str(stud.getIDStudent()))

    def __print_all_discipline(self):
        """
        Afiseaza toate disciplinele
        """
        dis_list = self.__srv_dis.get_all_discipline()
        if len(dis_list) == 0:
            print('Nu exista discipline in lista.')
        else:
            print('Lista de discipline este:')
            for dis in dis_list:
                # print('Nume disciplina: ', dis.getNume(), ' - Id disciplina: ', str(dis.getIDDisciplina()), ' - Profesor: ', dis.getProfesor())
                print('Nume disciplina: ', dis_list[dis].getNume(), ' - Id disciplina: ',
                      str(dis_list[dis].getIDDisciplina()),' - Profesor: ', dis_list[dis].getProfesor())

    def __print_note(self):
        """
        Afiseaza otoate notele
        """
        note_list = self.__srv_nota.get_all_note()
        if len(note_list) == 0:
            print('Nu exista note in lista.')
        else:
            print('Lista de note este: ')
            for nota in note_list:
                print(nota)

    def __add_student(self):
        """
        Adauga un student cu datele citite de la tastatura
        """
        nume = input("Numele studentului: ")
        try:
            id_student = int(input("Id-ul studentului: "))
        except ValueError:
            print('Id-ul studentului trebuie sa fie un numar mai mare decat 0.')
            return

        try:
            added_stud = self.__srv_stud.add_student(nume, id_student)
            print('Studentul ' + added_stud.getNume() + ' (' + str(added_stud.getIDStudent())
                  + ') a fost adaugat cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __add_disciplina(self):
        """
        Adauga o disciplina cu datele citite de la tastatura
        """
        nume = input("Numele disciplinei: ")
        try:
            id_disciplina = int(input("Id-ul disciplinei: "))
            profesor = input("Numele profesorului: ")
        except ValueError:
            print('Id-ul disciplinei trebuie sa fie un numar mai mare decat 0, iar numele profesorului trebuie sa '
                  'contina minim 2 caractere.')
            return

        try:
            added_dis = self.__srv_dis.add_disciplina(nume, id_disciplina, profesor)
            print('Disciplina ' + added_dis.getNume() + ' (' + str(added_dis.getIDDisciplina()) + ' , ' +
                added_dis.getProfesor() + ') a fost adaugata cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __delete_student(self):
        """
        Sterge un student cu datele citite de la tastatura
        """
        try:
            id_student = int(input("Id-ul studentului: "))
        except ValueError:
            print('Id-ul studentului trebuie sa fie un numar mai mare decat 0.')
            return

        try:
            deleted_stud = self.__srv_stud.delete_student(id_student)
            return deleted_stud
        except ValueError as ve:
            print(str(ve))
            return

    def __delete_disciplina(self):
        """
        Sterge o disciplina cu datele citite de la tastatura
        """
        try:
            id_disciplina = int(input("Id-ul disciplinei: "))
        except ValueError:
            print('Id-ul disciplinei trebuie sa fie un numar mai mare decat 0.')
            return

        try:
            deleted_dis = self.__srv_dis.delete_disciplina(id_disciplina)
            return deleted_dis
        except ValueError as ve:
            print(str(ve))
            return

    def __update_student(self):
        """
        Modifica datele unui student cu id-ul dat
        """
        try:
            id_student = int(input('ID-ul studentului:'))
        except ValueError:
            print('Id-ul studentului trebuie sa fie int.')
            return

        try:
            nume = input('Numele studentului: ')
        except ValueError:
            print('Numele studentului trebuie sa contina minim 2 caractere.')
        try:
            modified_stud = self.__srv_stud.update_student(id_student, nume)
            print('Studentul ' + modified_stud.getNume() + ' (' + str(modified_stud.getIDStudent())
                + ') a fost modificat cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __update_disciplina(self):
        """
        Modifica datele unei discipline cu id-ul dat
        """
        try:
            id_disciplina = int(input('ID-ul disciplinei: '))
        except ValueError:
            print('Id-ul disciplinei trebuie sa fie int.')
            return

        try:
            nume = input('Numele disciplinei: ')
            profesor = input('Numele profesorului: ')
        except ValueError:
            print('Numele disciplinei si al profesorului trebuie sa contina minim 2 caractere.')
        try:
            modified_dis = self.__srv_dis.update_disciplina(id_disciplina, nume, profesor)
            print('Disciplina ' + modified_dis.getNume() + ' (' + str(modified_dis.getIDDisciplina()) + ' , ' +
                modified_dis.getProfesor() + ') a fost adaugata cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __search_student(self):
        """
        Cauta un student cu id-ul dat
        """
        try:
            id_student = int(input('ID-ul studentului:'))
        except ValueError:
            print('Id-ul studentului trebuie sa fie int.')
            return

        try:
            stud = self.__srv_stud.search_student(id_student)
            print('Studentul cautat este:\nNume student: ', stud.getNume(), ' - Id student: ', str(stud.getIDStudent()))
        except ValueError as ve:
            print(str(ve))
            return

    def __search_disciplina(self):
        """
        Cauta o disciplina cu id-ul dat
        """
        try:
            id_disciplina = int(input('ID-ul disciplinei: '))
        except ValueError:
            print('Id-ul disciplinei trebuie sa fie int.')
            return

        try:
            dis = self.__srv_dis.search_disciplina(id_disciplina)
            print('Disciplina cautata este:\nNume disciplina: ', dis.getNume(), ' - Id disciplina: ',
                  str(dis.getIDDisciplina()), ' - Profesor: ', dis.getProfesor())
        except ValueError as ve:
            print(str(ve))
            return

    def __assign_nota(self):
        try:
            id_stud = int(input('Id-ul studentului:'))
            id_dis = int(input('Id-ul discipinei: '))
        except ValueError:
            print('Id-urile trebuie sa fie de tip int.')
            return

        try:
            nota_acordata = float(input('Nota acordata: '))
            nota = self.__srv_nota.create_nota(id_stud, id_dis, nota_acordata)
            print('Nota ', nota, ' a fost adaugata cu succes.')
        except ValueError as ve:
            print(str(ve))
            return

    def __ordonare(self):
        """
        Ordoneaza lista de studenti alfabetic si lista de note crescator la o disciplina data
        """
        try:
            id_dis = int(input('Id-ul discipinei: '))
        except ValueError:
            print('Id-ul trebuie sa fie de tip int.')
            return

        try:
            dis = self.__srv_dis.search_disciplina(id_dis)
            list_stud_nota = self.__srv_nota.ordonare(dis)
            for stud_nota in list_stud_nota:
                print('Student: ' + str(stud_nota[0].getNume()) + ' - ' + 'Nota: ' + str(stud_nota[1]))
        except ValueError as ve:
            print(str(ve))
            return

    def __medie(self):
        """
        Primi 20% dintre studenti ordonati dupa media notelor la toate disciplinele
        """
        try:
            list_stud = self.__srv_stud.get_all_students()
            list_medie = self.__srv_nota.medie(list_stud)
            for medie in list_medie:
                print('Student: ' + str(medie[1].getNume()) + ' - ' + 'Media: ' + str(medie[0]))
        except ValueError as ve:
            print(str(ve))
            return

    def __top_3(self):
        """
        Primi 3 studenti ordonati dupa medie
        """
        # try:
            # id_dis = int(input('Id-ul discipinei: '))
        # except ValueError:
            # print('Id-ul trebuie sa fie de tip int.')
            # return

        try:
            # dis = self.__srv_dis.search_disciplina(id_dis)
            list_stud = self.__srv_stud.get_all_students()
            # list_top_3 = self.__srv_medie.top_3(dis, list_stud, list_note)
            list_top_3 = self.__srv_nota.top_3(list_stud)
            for top_3 in list_top_3:
                print('Student: ' + str(top_3[1].getNume()) + ' - ' + 'Media: ' + str(top_3[0]))
        except ValueError as ve:
            print(str(ve))
            return

    def print_all_students_recursiv(self, all_stud):
        """
        Afiseaza lista de studenti recursiv
        :param all_stud: lista de studenti
        :type all_stud: list of Student object
        """
        if not all_stud:
            return
        print('Nume student: ', all_stud[0].getNume(), ' - Id student: ', str(all_stud[0].getIDStudent()))
        return self.print_all_students_recursiv(all_stud[1:])

    def search_student_recursiv(self):
        """
        Cauta un student cu id-ul dat recursiv
        """
        try:
            id_student = int(input('ID-ul studentului:'))
        except ValueError:
            print('Id-ul studentului trebuie sa fie int.')
            return

        try:
            all_stud = self.__srv_stud.get_all_students()
            stud = self.__srv_stud.search_student_recursiv(id_student, all_stud)
            print('Studentul cautat este:\nNume student: ', stud.getNume(), ' - Id student: ', str(stud.getIDStudent()))
        except ValueError as ve:
            print(str(ve))
            return

    def selection_sort(self):
        """
        Sorteaza lista de studenti dupa ID prin metoda sortarii prin selectie
        """
        try:
            list_stud = self.__srv_stud.selection_sotred()
            for stud in list_stud:
                print('Id student: ', str(stud.getIDStudent()), ' - Nume student: ', stud.getNume())
        except ValueError as ve:
            print(str(ve))
            return

    def shake_sort(self):
        """
        Sorteaza lista de studenti alfabetic prin metoda shake sort
        """
        try:
            # list_note = self.__srv_nota.sortare_shake()
            # for nota in list_note:
            #     print('Studentul:', nota.getStudent().getNume(), '- Nota: ', nota.getNota())
            list_stud = self.__srv_stud.sortare_shake()
            for stud in list_stud:
                print('- Nume student: ', stud.getNume(), 'Id student: ', str(stud.getIDStudent()))
        except ValueError as ve:
            print(str(ve))
            return

    def selectionsort(self):
        """
        Sorteaza lista de note dupa 2 criterii: alfabetic si dupa media notelor studentului
        """
        try:
            list_note = self.__srv_nota.selectionsort()
            for nota in list_note:
                print("Studentul: ", nota.getStudent().getNume(), " - Nota: ", nota.getNota())
        except ValueError as ve:
            print(str(ve))
            return

    def catalog_ui(self):
        # stud_list = self.__srv_stud.generate_list()
        # stud_list = self.__srv_stud.generate()
        # dis_list = self.__srv_dis.generate()
        # nota_list = self.__srv_nota.generate()
        while True:
            self.__print_menu()
            cmd = input('Comanda este:')
            cmd = cmd.lower().strip()
            if cmd == '11':
                self.__add_student()
            elif cmd == '12':
                self.__delete_student()
            elif cmd == '13':
                self.__update_student()
            elif cmd == '14':
                # self.__search_student()
                self.search_student_recursiv()
            elif cmd == '15':
                # self.__print_all_students()
                all_stud = self.__srv_stud.get_all_students()
                self.print_all_students_recursiv(all_stud)

            elif cmd == '21':
                self.__add_disciplina()
            elif cmd == '22':
                self.__delete_disciplina()
            elif cmd == '23':
                self.__update_disciplina()
            elif cmd == '24':
                self.__search_disciplina()
            elif cmd == '25':
                self.__print_all_discipline()

            elif cmd == '31':
                self.__assign_nota()
            elif cmd == '32':
                self.__print_note()
            elif cmd == '33':
                self.__ordonare()
            elif cmd == '34':
                self.__medie()
            elif cmd == '35':
                self.__top_3()

            elif cmd == '1':
                self.selection_sort()
            elif cmd == '2':
                self.shake_sort()
            elif cmd == '3':
                self.selectionsort()

            elif cmd == 'x':
                return
            else:
                print('Comanda invalida.')
