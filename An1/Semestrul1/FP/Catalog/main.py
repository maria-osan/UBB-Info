from domain.validators import StudentValidator, DisciplinaValidator, NotaValidator

from repository.disciplina_repo import InMemoryRepositoryDisciplina, DisciplinaFileRepo
from repository.student_repo import InMemoryRepositoryStudent, StudentFileRepo
from repository.nota_repo import InMemoryRepositoryNota, NotaFileRepo

from service.student_service import StudentService
from service.disciplina_service import DisciplinaService
from service.nota_service import NotaService

from ui.console import Console

# repo_stud = InMemoryRepositoryStudent()
repo_file_stud = StudentFileRepo('data\students.txt')
val_stud = StudentValidator()
srv_stud = StudentService(repo_file_stud, val_stud)

# repo_dis = InMemoryRepositoryDisciplina()
repo_file_dis = DisciplinaFileRepo('data\discipline.txt')
val_dis = DisciplinaValidator()
srv_dis = DisciplinaService(repo_file_dis, val_dis)

# repo_nota = InMemoryRepositoryNota()
repo_file_nota = NotaFileRepo('data\\note.txt')
val_nota = NotaValidator()
srv_nota = NotaService(repo_file_nota, val_nota, repo_file_stud, repo_file_dis)

ui = Console(srv_stud, srv_dis, srv_nota)
ui.catalog_ui()
