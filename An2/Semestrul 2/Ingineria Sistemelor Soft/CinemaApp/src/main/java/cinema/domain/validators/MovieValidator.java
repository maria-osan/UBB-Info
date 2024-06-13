package cinema.domain.validators;

import cinema.domain.Movie;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Arrays;
import java.util.List;

public class MovieValidator implements Validator<Movie> {
    @Override
    public void validate(Movie entity) throws ValidationException {
        validateName(entity.getName());
        validateGenre(entity.getGenre());
        validateDate(entity.getMovieDate());
        validateTime(entity.getMovieTime());
    }

    private void validateName(String name) throws ValidationException {
        if(name == null)
            throw new ValidationException("Invalid name - it is null!");
        else if(name.isEmpty())
            throw new ValidationException("Invalid name - it is empty!");
    }

    private void validateGenre(String genre) throws ValidationException {
        if(genre == null)
            throw new ValidationException("Invalid genre - it is null!");
        else if(genre.isEmpty())
            throw new ValidationException("Invalid genre - it is empty!");
        else if(! genre.matches("[a-zA-Z]+"))
            throw new ValidationException("Invalid genre - must contain only letters!");

        List<String> genres = Arrays.asList("action", "comedy", "drama", "horror", "science fiction", "sf", "fantasy", "romance",
        "thriller", "adventure", "mystery", "animation", "documentary", "musical", "western", "war", "fiction");
        String lowercaseGenre = genre.toLowerCase();
        if (genres.stream().map(String::toLowerCase).noneMatch(lowercaseGenre::equals)) {
            throw new ValidationException("Invalid genre - '" + genre + "' not in the allowed genre list!");
        }
    }

    private void validateDate(LocalDate date) throws ValidationException {
        if(date == null)
            throw new ValidationException("Invalid date - it is null!");
        else if(date.isBefore(LocalDate.now()))
            throw new ValidationException("Invalid date - the date has passed!");
    }

    private void validateTime(LocalTime time) throws ValidationException {
        if(time == null)
            throw new ValidationException("Invalid time - it is null!");
        if(time.isBefore(LocalTime.of(12, 0)) || time.isAfter(LocalTime.of(22, 0)))
            throw new ValidationException("Invalid time - it is outside working hours!");
    }
}
