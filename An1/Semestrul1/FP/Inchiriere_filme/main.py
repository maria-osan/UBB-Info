from domain.validators import ClientValidator
from domain.validators import MovieValidator

from repository.client_repo import ClientFileRepo
from repository.movie_repo import MovieFileRepo

from service.client_service import ClientService
from service.movie_service import MovieService

from ui.console import Console

repo_file_client = ClientFileRepo('clients.txt')
val_client = ClientValidator()
srv_client = ClientService(val_client, repo_file_client)

repo_file_movie = MovieFileRepo('movie.txt')
val_movie = MovieValidator
srv_movie = MovieService(repo_file_movie, val_movie)

ui = Console(srv_client, srv_movie)

ui.inchiriere_ui()
