class ClientValidator:
    def validate_client(self, client):
        """
        Verifica datele unui client
        """
        errors = []
        if len(client.get_nume()) < 2:
            errors.append('Numele clientului trebuie ca contina mai mult de doua caractere.')
        if client.get_id() < 0:
            errors.append('Id-ul clientului trebuie sa fie un numar pozitiv.')
        if int(int(client.get_cnp())/10000000000000) < 0 or int(int(client.get_cnp())/10000000000000) > 9:
            errors.append('CNP-ul clientului trebuie sa contina fix 13 cifre.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)


class MovieValidator:
    def validate_movie(self, movie):
        """
        Verifica datele unui film
        :type movie: Movie
        """
        errors = []
        if movie.get_id() < 0:
            errors.append('ID-ul filmului trebuie sa fie un numar pozitiv.')
        if len(movie.get_titlu()) < 2:
            errors.append('Titlul filmului trebuie sa fie de minim 2 caractere.')
        if len(movie.get_descriere()) < 10:
            errors.append('Descrierea filmului trebuie sa contina minim 10 caractere.')
        if len(movie.get_gen()) < 1:
            errors.append('Genul filmului trebuie sa contina minim 1 caractere.')

        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)

# teste
