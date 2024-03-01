import unittest

from domain.entities import Student
from domain.validators import StudentValidator


class TestCaseDisciplinaDomain(unittest.TestCase):
    def setUp(self) -> None:
        self.__validator = StudentValidator()

    def test_create_disciplina(self):
        stud1 = Student('Ema Pop', 1236)
        self.assertEqual(stud1.getNume(), 'Ema Pop')
        self.assertEqual(stud1.getIDStudent(), 1236)

        stud1.setNume('Denisa Moldovan')
        stud1.setIDStudent(478)

        self.assertEqual(stud1.getNume(), 'Denisa Moldovan')
        self.assertEqual(stud1.getIDStudent(), 478)

    def test_equals_disciplina(self):
        stud1 = Student('Ema Pop', 1236)
        stud2 = Student('Ema Pop', 1236)

        self.assertEqual(stud1, stud2)

        stud3 = Student('Ema Pop', 12)
        self.assertNotEqual(stud1, stud3)

    def test_disciplina_validator(self):
        stud1 = Student('Ema Pop', 1236)
        self.__validator.validate_stud(stud1)
