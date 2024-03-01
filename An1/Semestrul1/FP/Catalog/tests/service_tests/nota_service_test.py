import unittest

from domain.validators import Student, Disciplina, Nota
from domain.validators import NotaValidator
from repository.student_repo import StudentFileRepo
from repository.disciplina_repo import DisciplinaFileRepo
from repository.nota_repo import NotaFileRepo
from service.nota_service import NotaService


class TestCaseNotaService(unittest.TestCase):
    def setUp(self) -> None:
        stud_repo = StudentFileRepo('test_student_service.txt')
        dis_repo = DisciplinaFileRepo('test_disciplina_service.txt')

        self.__initializare_note_file()

        nota_repo = NotaFileRepo('test_nota_service.txt')
        nota_val = NotaValidator

        self.__srv = NotaService(nota_repo, nota_val, stud_repo, dis_repo)
        self.__repo = NotaFileRepo('test_nota_service.txt')

    def __initializare_note_file(self):
        with open('original_note.txt', 'r') as f:
            with open('test_nota_service.txt', 'w') as f1:
                f1.write(f.read())

    def test_create_nota(self):
        stud = Student('Ema Pop', 1236)
        dis = Disciplina('Matematica', 5, 'Dana Morar')
        created_nota = self.__srv.create_nota(stud.getIDStudent(), dis.getIDDisciplina(), 8.75)

        self.assertEqual(created_nota.getStudent().getNume(), 'Ema Pop')
        self.assertEqual(created_nota.getDisciplina().getNume(), 'Matematica')
        self.assertEqual(created_nota.getNota(), 8.75)

    def test_get_all_note(self):
        crt_note = self.__srv.get_all_note()
        self.assertIsInstance(crt_note, list)
        self.assertEqual(len(crt_note), 0)

    def tearDown(self) -> None:
        self.__repo.delete_all()
