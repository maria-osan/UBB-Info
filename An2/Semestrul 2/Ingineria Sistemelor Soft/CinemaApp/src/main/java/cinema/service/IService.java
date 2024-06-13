package cinema.service;

import cinema.domain.Movie;
import cinema.domain.Seat;
import cinema.domain.User;

import java.util.List;

public interface IService {
    boolean handleLogin(String username, String password);
    void handleSignUp(String name, String email, String username, String password, boolean isAdmin);
    void handleLogout(User user);

    Movie getTodayMovie();
    float handleReservation(User user, List<Seat> seats);

    void addMovie(Movie movie);
    void updateMovie(Movie movie);
    void deleteMovie(Long id);

    void checkAndResetSeatAvailability();

    User findByUsername(String username);
    Iterable<Movie> getAllMovies();
    Seat findSeatByNr(String nr);
    Iterable<Seat> getAllSeats();
}
