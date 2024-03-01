from domain.entities import Student, Disciplina, Nota
from exceptions.exceptions import ValidationException


class StudentValidator:
    def validate_stud(self, stud):
        errors = []
        if len(stud.getNume()) < 2:
            errors.append('Numele studentului trebuie sa aiba mai mult de 2 caractere.')
        if stud.getIDStudent() < 0:
            errors.append('Id-ul studentului trebuie sa fie mai mare de 0.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


class DisciplinaValidator:
    def validate_dis(self, dis):
        errors = []
        if len(dis.getNume()) < 2:
            errors.append('Numele disciplinei trebuie sa aiba mai mult de 2 caractere.')
        if dis.getIDDisciplina() < 0:
            errors.append('Id-ul disciplinei trebuie sa fie mai mare de 0.')
        if len(dis.getProfesor()) < 2:
            errors.append('Numele profesorului trebuie sa aiba mai mult de 2 caractere.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


class NotaValidator:
    def validate_nota(self, nota):
        errors = []
        if nota.getNota() < 1 or nota.getNota() > 10:
            errors.append('Nota trebuie sa fie intre 1 si 10.')

        if len(errors) > 0:
            raise ValidationException(errors)


def test_student_validator():
    test_validator = StudentValidator()
    stud1 = Student('Ema Pop', 1236)
    test_validator.validate_stud(stud1)
    stud2 = Student('', 2050)

    try:
        test_validator.validate_stud(stud2)
        assert False
    except ValueError:
        assert True

    stud3 = Student('Ana Hagau', -55)
    try:
        test_validator.validate_stud(stud3)
        assert False
    except ValueError:
        assert True


def test_disciplina_validator():
    test_validator = DisciplinaValidator()
    dis1 = Disciplina('Matematica', 5629, 'Dana Rosca')
    test_validator.validate_dis(dis1)
    dis2 = Disciplina('', -29, 'Delia Bodor')

    try:
        test_validator.validate_dis(dis2)
        assert False
    except ValueError:
        assert True

    dis3 = Disciplina('Desen', 8762, '')
    try:
        test_validator.validate_dis(dis3)
        assert False
    except ValueError:
        assert True


def test_nota_validator():
    test_validator = NotaValidator()
    stud = Student('Ema Pop', 1236)
    dis = Disciplina('Matematica', 5629, 'Dana Rosca')
    nota1 = Nota(stud, dis, 8.75)
    test_validator.validate_nota(nota1)

    nota2 = Nota(stud, dis, 10.45)
    try:
        test_validator.validate_nota(nota2)
        assert False
    except ValidationException:
        assert True

    nota3 = Nota(stud, dis, -0.5)
    try:
        test_validator.validate_nota(nota3)
        assert False
    except ValidationException:
        assert True


test_student_validator()
test_disciplina_validator()
test_nota_validator()
