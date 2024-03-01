from domain.entities import Movie


class MovieFileRepo:
    def __init__(self, filename):
        self.__filenale = filename

    def __load_from_file(self):
        """
        Incarca datele din fisier
        """
        try:
            f = open(self.__filenale, 'r')
        except IOError:
            return

        all_movies = []
        lines = f.readlines()
        for line in lines:
            id_movie, titlu, descriere, gen = [token.strip() for token in line.split(';')]
            id_movie = int(id_movie)
            movie = Movie(id_movie, titlu, descriere, gen)
            all_movies.append(movie)

        f.close()
        return all_movies

    def __save_to_file(self, all_movie):
        """
        Salveaza datele in fisier
        :param all_movie: lista de filme
        :type all_movie: list of Movie objects
        """
        with open(self.__filenale, 'w') as f:
            for movie in all_movie:
                movie_string = str(movie.get_id()) + ';' + str(movie.get_titlu()) + ';' + str(movie.get_descriere()) + ';' + str(movie.get_gen()) + '\n'
                f.write(movie_string)