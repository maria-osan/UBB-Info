import unittest

from domain.entities import Student, Disciplina, Nota
from repository.nota_repo import NotaFileRepo


class TestCaseNotaFileRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = NotaFileRepo('test_nota_repo.txt')

    def test_store(self):
        stud = Student('Ema Pop', 1236)
        dis = Disciplina('Matematica', 5, 'Dana Morar')
        nota = Nota(stud, dis, 8.75)

        self.__repo.store_nota(nota)
        self.assertEqual(self.__repo.size(), 1)

    def test_find(self):
        stud1 = Student('Ana Hagau', 2015)
        stud2 = Student('Alex Baciu', 473)
        stud3 = Student('Florin Coroiu', 908)

        dis1 = Disciplina('Desen', 8762, 'Delia Bodor')
        dis2 = Disciplina('Romana', 5629, 'Anca Morari')

        nota1 = Nota(stud1, dis1, 9.90)
        nota2 = Nota(stud2, dis2, 9.05)
        nota3 = Nota(stud3, dis2, 9.45)

        self.__repo.store_nota(nota1)
        self.__repo.store_nota(nota2)

        self.assertIs(self.__repo.find_nota(nota3), None)

    def test_get_all(self):
        crt_note = self.__repo.get_all_note()
        self.assertIsInstance(crt_note, list)
        self.assertEqual(len(crt_note), 0)

    def test_size(self):
        self.assertEqual(self.__repo.size(), 0)

        stud3 = Student('Florin Coroiu', 908)
        dis2 = Disciplina('Romana', 5629, 'Anca Morari')
        nota3 = Nota(stud3, dis2, 9.45)

        self.__repo.store_nota(nota3)
        self.assertEqual(self.__repo.size(), 1)

    def tearDown(self) -> None:
        self.__repo.delete_all()
