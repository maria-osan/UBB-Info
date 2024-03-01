import unittest

from domain.entities import Student
from repository.student_repo import StudentFileRepo


class TestCaseStudentRepoFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = StudentFileRepo('test_student_repo.txt')
        self.__add_predefined_students()

    def __add_predefined_students(self):
        stud1 = Student('Ema Pop', 1236)
        stud2 = Student('Ana Hagau', 2015)
        stud3 = Student('Nadia Maxim', 1547)
        stud4 = Student('Alex Baciu', 473)
        stud5 = Student('Florin Coroiu', 908)

        self.__repo.store_student(stud1)
        self.__repo.store_student(stud2)
        self.__repo.store_student(stud3)
        self.__repo.store_student(stud4)
        self.__repo.store_student(stud5)

    def test_find(self):
        p = self.__repo.find_student(1236)
        self.assertEqual(p.getNume(), 'Ema Pop')

        p1 = self.__repo.find_student(47)
        self.assertIs(p1, None)

    def test_size(self):
        self.assertEqual(self.__repo.size(), 5)

        self.__repo.delete_student(1547)
        self.__repo.delete_student(2015)

        self.assertEqual(self.__repo.size(), 3)

        self.__repo.store_student(Student('Denisa Moldovan', 46))
        self.assertEqual(self.__repo.size(), 4)
        self.__repo.update(908, Student('Radu Duma', 473))
        self.assertEqual(self.__repo.size(), 4)

    def test_get_all(self):
        crt_students = self.__repo.get_all_students()
        self.assertIsInstance(crt_students, list)

        self.assertEqual(len(crt_students), 5)

        self.__repo.delete_student(1547)
        self.__repo.delete_student(2015)

        crt_students = self.__repo.get_all_students()
        self.assertEqual(len(crt_students), 3)

    def test_store(self):
        initial_size = self.__repo.size()
        stud1 = Student('Denisa Moldovan', 46)
        self.__repo.store_student(stud1)

        self.assertEqual(self.__repo.size(), initial_size+1)
        stud2 = Student('Radu Duma', 305)
        self.__repo.store_student(stud2)
        self.assertEqual(self.__repo.size(), initial_size+2)

    def test_delete(self):
        initial_size = self.__repo.size()
        deleted_stud = self.__repo.delete_student(1547)
        self.assertTrue(deleted_stud.getNume() == 'Nadia Maxim')
        self.assertTrue(self.__repo.size() == initial_size-1)

    def test_update(self):
        stud1 = Student('Denisa Moldovan', 1547)

        modified_stud = self.__repo.update(1547, stud1)
        self.assertEqual(modified_stud.getNume(), 'Denisa Moldovan')

    def tearDown(self) -> None:
        self.__repo.delete_all()
