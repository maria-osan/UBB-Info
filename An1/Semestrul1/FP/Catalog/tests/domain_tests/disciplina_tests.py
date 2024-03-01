import unittest

from domain.entities import Disciplina
from domain.validators import DisciplinaValidator


class TestCaseDisciplinaDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = DisciplinaValidator()

    def test_create_disciplina(self):
        dis1 = Disciplina('Matematica', 5, 'Dana Morar')
        self.assertEqual(dis1.getNume(), 'Matematica')
        self.assertEqual(dis1.getIDDisciplina(), 5)
        self.assertEqual(dis1.getProfesor(), 'Dana Morar')

        dis1.setNume('Engleza')
        dis1.setIDDisciplina(2001)
        dis1.setProfesor('Claudia Popescu')

        self.assertEqual(dis1.getNume(), 'Engleza')
        self.assertEqual(dis1.getIDDisciplina(), 2001)
        self.assertEqual(dis1.getProfesor(), 'Claudia Popescu')

    def test_equals_disciplina(self):
        dis1 = Disciplina('Matematica', 5, 'Dana Morar')
        dis2 = Disciplina('Matematica', 5, 'Dana Morar')

        self.assertEqual(dis1, dis2)

        dis3 = Disciplina('Matematica', 6, 'Dana Morar')
        self.assertNotEqual(dis1, dis3)

    def test_disciplina_validator(self):
        dis1 = Disciplina('Matematica', 5, 'Dana Morar')
        self.__validator.validate_dis(dis1)
