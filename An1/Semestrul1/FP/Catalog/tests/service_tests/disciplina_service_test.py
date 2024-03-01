import unittest

from domain.validators import DisciplinaValidator
from repository.disciplina_repo import DisciplinaFileRepo
from service.disciplina_service import DisciplinaService


class TestCaseDisciplinaService(unittest.TestCase):
    def setUp(self) -> None:
        repo = DisciplinaFileRepo('test_disciplina_service.txt')
        validator = DisciplinaValidator
        self.__srv = DisciplinaService(repo, validator)
        self.__repo = DisciplinaFileRepo('test_disciplina_service.txt')

    def test_add_disciplina(self):
        added_dis = self.__srv.add_disciplina('Matematica', 5, 'Dana Morar')
        self.assertTrue(added_dis.getNume() == 'Matematica')
        self.assertTrue(added_dis.getIDDisciplina() == 5)
        self.assertTrue(added_dis.getProfesor() == 'Dana Morar')

        self.assertEqual(len(self.__srv.get_all_discipline()), 1)

    def test_delete_disciplina(self):
        self.__srv.add_disciplina('Matematica', 5, 'Dana Morar')
        deleted_dis = self.__srv.delete_disciplina(5)

        self.assertEqual(len(self.__srv.get_all_discipline()), 0)
        self.assertEqual(deleted_dis.getNume(), 'Matematica')

    def test_get_all_disciplina(self):
        self.__srv.add_disciplina('Matematica', 5, 'Dana Morar')
        self.__srv.add_disciplina('Engleza', 2001, 'Claudia Popescu')
        self.assertIsInstance(self.__srv.get_all_discipline(), dict)
        self.assertEqual(len(self.__srv.get_all_discipline()), 2)

    def test_update_disciplina(self):
        self.__srv.add_disciplina('Matematica', 5, 'Dana Morar')
        updated_dis = self.__srv.update_disciplina(5, 'Engleza', 'Claudia Popescu')

        self.assertTrue(updated_dis.getNume() == 'Engleza')
        self.assertTrue(updated_dis.getProfesor() == 'Claudia Popescu')

    def tearDown(self) -> None:
        self.__repo.delete_all()
