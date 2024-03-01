import unittest

from domain.entities import Disciplina
from repository.disciplina_repo import DisciplinaFileRepo


class TestCaseDisciplinaRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = DisciplinaFileRepo('test_disciplina_repo.txt')
        self.__populate_list()

    def __populate_list(self):
        dis1 = Disciplina('Matematica', 5, 'Dana Morar')
        dis2 = Disciplina('Desen', 8762, 'Delia Bodor')
        dis3 = Disciplina('Romana', 5629, 'Anca Morari')

        self.__repo.store_disciplina(dis1)
        self.__repo.store_disciplina(dis2)
        self.__repo.store_disciplina(dis3)

    def test_find(self):
        p = self.__repo.find_disciplina(5)
        self.assertTrue(p.getNume() == 'Matematica')
        self.assertTrue(p.getProfesor() == 'Dana Morar')

        p1 = self.__repo.find_disciplina(256)
        self.assertIs(p1, None)

    def test_size(self):
        initial_size = self.__repo.size()
        self.__repo.delete_disciplina(8762)

        self.assertEqual(self.__repo.size(), initial_size-1)

        self.__repo.store_disciplina(Disciplina('Informatica', 45601, 'Elena Tivadar'))
        self.assertEqual(self.__repo.size(), initial_size)
        self.__repo.update(5629, Disciplina('Engleza', 5629, 'Claudia Popescu'))
        self.assertEqual(self.__repo.size(), initial_size)

    def test_get_all(self):
        initial_size = self.__repo.size()
        crt_discipline = self.__repo.get_all_discipline()
        self.assertIsInstance(crt_discipline, dict)

        self.assertEqual(len(crt_discipline), initial_size)

        self.__repo.delete_disciplina(8762)

        crt_discipline = self.__repo.get_all_discipline()
        self.assertEqual(len(crt_discipline), initial_size-1)

        self.__repo.store_disciplina(Disciplina('Informatica', 45601, 'Elena Tivadar'))
        self.__repo.store_disciplina(Disciplina('Engleza', 2001, 'Claudia Popescu'))
        self.assertTrue(self.__repo.size() == initial_size+1)

        self.__repo.update(2001, Disciplina('Desen',2001, 'Delia Bodor'))
        self.assertTrue(self.__repo.size() == initial_size+1)

    def test_store(self):
        initial_size = self.__repo.size()
        dis1 = Disciplina('Logica', 601, 'Angela Coroiu')
        self.__repo.store_disciplina(dis1)

        self.assertEqual(self.__repo.size(), initial_size+1)
        dis2 = Disciplina('Antreprenoriala', 123, 'Marcel Rus')
        self.__repo.store_disciplina(dis2)
        self.assertEqual(self.__repo.size(), initial_size+2)

    def test_delete(self):
        initial_size = self.__repo.size()
        deleted_dis = self.__repo.delete_disciplina(8762)
        self.assertTrue(deleted_dis.getNume() == 'Desen')
        self.assertTrue(self.__repo.size() == initial_size-1)

    def test_update(self):
        dis1 = Disciplina('Antreprenoriala', 123, 'Marcel Rus')
        self.__repo.store_disciplina(dis1)
        dis2 = Disciplina('Antreprenoriala', 123, 'Irina Rusu')

        modified_dis = self.__repo.update(123, dis2)
        self.assertEqual(modified_dis.getNume(), 'Antreprenoriala')
        self.assertEqual(modified_dis.getProfesor(), 'Irina Rusu')

    def tearDown(self) -> None:
        self.__repo.delete_all()
