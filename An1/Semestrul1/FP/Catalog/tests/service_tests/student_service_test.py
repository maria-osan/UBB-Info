import unittest

from domain.validators import StudentValidator
from repository.student_repo import StudentFileRepo
from service.student_service import StudentService


class TestCaseStudentService(unittest.TestCase):
    def setUp(self) -> None:
        repo = StudentFileRepo('test_student_service.txt')
        validator = StudentValidator
        self.__srv = StudentService(repo, validator)
        self.__repo = StudentFileRepo('test_student_service.txt')

    def test_add_student(self):
        added_stud = self.__srv.add_student('Ema Pop', 1236)
        self.assertTrue(added_stud.getNume() == 'Ema Pop')
        self.assertTrue(added_stud.getIDStudent() == 1236)

        self.assertEqual(len(self.__srv.get_all_students()), 1)

    def test_delete_student(self):
        self.__srv.add_student('Ema Pop', 1236)
        deleted_stud = self.__srv.delete_student(1236)

        self.assertEqual(len(self.__srv.get_all_students()), 0)
        self.assertTrue(deleted_stud.getNume() == 'Ema Pop')
        self.assertTrue(deleted_stud.getIDStudent() == 1236)

    def test_get_all_students(self):
        self.__srv.add_student('Alex Baciu', 473)
        self.__srv.add_student('Denisa Moldovan', 46)
        self.assertIsInstance(self.__srv.get_all_students(), list)
        self.assertEqual(len(self.__srv.get_all_students()), 2)

    def test_update_student(self):
        self.__srv.add_student('Ema Pop', 1236)
        updated_stud = self.__srv.update_student(1236, 'Denisa Moldovan')

        self.assertTrue(updated_stud.getNume() == 'Denisa Moldovan')

    def tearDown(self) -> None:
        self.__repo.delete_all()
