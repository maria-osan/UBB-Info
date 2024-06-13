package cinema.service;

import cinema.domain.Movie;
import cinema.domain.Seat;
import cinema.domain.Ticket;
import cinema.domain.User;
import cinema.domain.validators.ValidationException;
import cinema.domain.validators.Validator;
import cinema.repository.IMovieRepository;
import cinema.repository.ISeatRepository;
import cinema.repository.ITicketRepository;
import cinema.repository.IUserRepository;
import cinema.utils.Observable;
import cinema.utils.Observer;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.*;

public class Service implements IService, Observable {
    private final IUserRepository userRepo;
    private final ISeatRepository seatRepo;
    private final IMovieRepository movieRepo;
    private final ITicketRepository ticketRepo;

    private final Validator<User> userValidator;
    private final Validator<Movie> movieValidator;

    private List<Observer> observers = new ArrayList<>();

    private final Set<String> loggedUsers = new HashSet<>();

    public Service(IUserRepository userRepo, ISeatRepository seatRepo, IMovieRepository movieRepo,
                   ITicketRepository ticketRepo, Validator<User> userValidator, Validator<Movie> movieValidator) {
        this.userRepo = userRepo;
        this.seatRepo = seatRepo;
        this.movieRepo = movieRepo;
        this.ticketRepo = ticketRepo;
        this.userValidator = userValidator;
        this.movieValidator = movieValidator;
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for(Observer observer : observers)
            observer.update();
    }

    @Override
    public boolean handleLogin(String username, String password) {
        User user = userRepo.findOne(username);

        if(user == null)
            throw new ValidationException("User not found!");
        else if(!Objects.equals(user.getPassword(), password))
            throw new ValidationException("Incorrect password!");
        else {
            for(String u : loggedUsers) {
                if(Objects.equals(username, u))
                    throw new ValidationException("User already logged!");
            }
        }

        loggedUsers.add(user.getUsername());
        return user.isAdmin();
    }

    @Override
    public void handleSignUp(String name, String email, String username, String password, boolean isAdmin) {
        User user = new User(name, email, username, password, isAdmin);
        try {
            userValidator.validate(user);
            userRepo.save(user);
            loggedUsers.add(username);
        } catch (ValidationException ex) {
            throw new ValidationException(ex.getMessage());
        }
    }

    @Override
    public void handleLogout(User user) {
        loggedUsers.remove(user.getUsername());
    }

    @Override
    public float handleReservation(User user, List<Seat> seats) {
        // Check if all seats are available
        for (Seat seat : seats) {
            Seat seatFromDB = seatRepo.findOne(seat.getNr());
            if (seatFromDB == null || !seatFromDB.isAvailable()) {
                throw new ValidationException("Seat " + seat.getNr() + " is not available.");
            }
        }

        // Calculate the total price of the seats
        float totalPrice = 0;
        for (Seat seat : seats) {
            totalPrice += seat.getPrice();
        }

        // Create a new ticket
        Movie todayMovie = getTodayMovie();
        Ticket ticket = new Ticket(user.getName(), todayMovie.getId(), totalPrice, seats);

        // Save the ticket to the database
        ticketRepo.save(ticket);

        // Mark the seats as reserved
        for (Seat seat : seats) {
            seat.setAvailable(false);
            seatRepo.update(seat);
        }

        // Notify observers about the seat reservation
        notifyObservers();

        return totalPrice;
    }

    @Override
    public Movie getTodayMovie() {
        return movieRepo.findOne(LocalDate.now());
    }

    @Override
    public void addMovie(Movie movie) {
        try {
            movieValidator.validate(movie);
            movieRepo.save(movie);

            notifyObservers();
        } catch (ValidationException ex) {
            throw new ValidationException(ex.getMessage());
        }
    }

    @Override
    public void updateMovie(Movie movie) {
        try{
            movieValidator.validate(movie);
            movieRepo.update(movie);

            notifyObservers();
        } catch (ValidationException ex) {
            throw new ValidationException(ex.getMessage());
        }
    }

    @Override
    public void deleteMovie(Long id) {
        movieRepo.delete(id);
        notifyObservers();
    }

    @Override
    public void checkAndResetSeatAvailability() {
        LocalTime currentTime = LocalTime.now();
        LocalTime noon = LocalTime.of(12, 0);

        if (currentTime.isBefore(noon)) {
            resetSeatAvailability();
            notifyObservers();  // Notify observers after resetting seat availability
        }
    }

    private void resetSeatAvailability() {
        Iterable<Seat> allSeats = seatRepo.findAll();
        for (Seat seat : allSeats) {
            seat.setAvailable(true);
            seatRepo.update(seat);
        }
    }

    @Override
    public User findByUsername(String username) {
        return userRepo.findOne(username);
    }

    @Override
    public Iterable<Movie> getAllMovies() {
        return movieRepo.findAll();
    }

    @Override
    public Seat findSeatByNr(String nr) {
        return seatRepo.findOne(nr);
    }

    @Override
    public Iterable<Seat> getAllSeats() {
        return seatRepo.findAll();
    }
}
