import unittest

from domain.validators import NotaValidator
from domain.entities import Student, Disciplina, Nota


class TestCaseNotaDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = NotaValidator()

    def test_create_nota(self):
        stud = Student('Ema Pop', 1236)
        dis = Disciplina('Matematica', 5, 'Dana Morar')

        nota = Nota(stud, dis, 9.05)

        self.assertEqual(nota.getStudent().getNume(), 'Ema Pop')
        self.assertEqual(nota.getStudent().getIDStudent(), 1236)
        self.assertEqual(nota.getDisciplina().getNume(), 'Matematica')
        self.assertEqual(nota.getDisciplina().getIDDisciplina(), 5)
        self.assertEqual(nota.getDisciplina().getProfesor(), 'Dana Morar')
        self.assertEqual(nota.getNota(), 9.05)

    def test_nota_validator(self):
        stud = Student('Ema Pop', 1236)
        dis = Disciplina('Matematica', 5, 'Dana Morar')

        nota = Nota(stud, dis, 9.05)

        self.__validator.validate_nota(nota)
