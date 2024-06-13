package cinema.repository;

import cinema.domain.Movie;

import java.time.LocalDate;

public interface IMovieRepository extends IRepository<Long, Movie> {
    Movie findOne(LocalDate date);
}
