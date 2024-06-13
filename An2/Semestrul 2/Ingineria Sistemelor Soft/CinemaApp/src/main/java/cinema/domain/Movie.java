package cinema.domain;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.Objects;

public class Movie extends Entity<Long> {
    private String name;
    private String genre;
    private LocalDate movieDate;
    private LocalTime movieTime;

    public Movie(String name, String genre, LocalDate movieDate, LocalTime movieTime) {
        this.name = name;
        this.genre = genre;
        this.movieDate = movieDate;
        this.movieTime = movieTime;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public LocalDate getMovieDate() {
        return movieDate;
    }

    public void setMovieDate(LocalDate movieDate) {
        this.movieDate = movieDate;
    }

    public LocalTime getMovieTime() {
        return movieTime;
    }

    public void setMovieTime(LocalTime movieTime) {
        this.movieTime = movieTime;
    }

    @Override
    public String toString() {
        return "Movie{" +
                "name='" + name + '\'' +
                ", genre='" + genre + '\'' +
                ", movieDate=" + movieDate +
                ", movieTime=" + movieTime +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Movie movie = (Movie) o;
        return Objects.equals(name, movie.name) && Objects.equals(genre, movie.genre) && Objects.equals(movieDate, movie.movieDate) && Objects.equals(movieTime, movie.movieTime);
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), name, genre, movieDate, movieTime);
    }
}
