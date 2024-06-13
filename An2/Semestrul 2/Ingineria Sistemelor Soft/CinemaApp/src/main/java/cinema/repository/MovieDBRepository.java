package cinema.repository;

import cinema.domain.Movie;

import java.sql.*;
import java.time.LocalDate;
import java.time.LocalTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class MovieDBRepository implements IMovieRepository{
    protected String url;
    protected String username;
    protected String password;

    public MovieDBRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Movie findOne(LocalDate date) {
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM movies WHERE movieDate = ?");)
        {
            statement.setDate(1, Date.valueOf(date));
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                long id = result.getLong("id");
                String name = result.getString("name");
                String genre = result.getString("genre");
                LocalTime time = result.getTime("movieTime").toLocalTime();
                Movie movie = new Movie(name, genre, date, time);
                movie.setId(id);
                return movie;
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding movie with date: " + date, e);
        }
        return null;
    }

    @Override
    public Movie findOne(Long id) {
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM movies WHERE id = ?");)
        {
            statement.setLong(1, id);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                String name = result.getString("name");
                String genre = result.getString("genre");
                LocalDate movieDate = result.getDate("movieDate").toLocalDate();
                LocalTime movieTime = result.getTime("movieTime").toLocalTime();
                Movie movie = new Movie(name, genre, movieDate, movieTime);
                movie.setId(id);
                return movie;
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding movie with id: " + id, e);
        }
        return null;
    }

    @Override
    public Iterable<Movie> findAll() {
        List<Movie> movies = new ArrayList<>();

        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM movies");
             ResultSet resultSet = statement.executeQuery()) {
            while (resultSet.next()) {
                long id = resultSet.getLong("id");
                String name = resultSet.getString("name");
                String genre = resultSet.getString("genre");
                LocalDate date = resultSet.getDate("movieDate").toLocalDate();
                LocalTime time = resultSet.getTime("movieTime").toLocalTime();
                Movie movie = new Movie(name, genre, date, time);
                movie.setId(id);
                movies.add(movie);
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding all movies", e);
        }

        return movies;
    }

    @Override
    public Optional<Movie> save(Movie entity) {
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement  = connection.prepareStatement("INSERT INTO movies (name, genre, movieDate, movieTime) VALUES (?, ?, ?, ?)");)
        {
            statement.setString(1, entity.getName());
            statement.setString(2, entity.getGenre());
            statement.setDate(3, Date.valueOf(entity.getMovieDate()));
            statement.setTime(4, Time.valueOf(entity.getMovieTime()));
            int affectedRows = statement.executeUpdate();
            return affectedRows!=0? Optional.empty():Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error saving movie: " + entity, e);
        }
    }

    @Override
    public Optional<Movie> delete(Long id) {
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement  = connection.prepareStatement("DELETE FROM movies WHERE id = ?");)
        {
            Optional<Movie> movie = Optional.ofNullable(findOne(id));
            statement.setLong(1,id);
            int affectedRows = statement.executeUpdate();
            return affectedRows==0? Optional.empty():movie;
        } catch (SQLException e) {
            throw new RuntimeException("Error deleting movie with id: " + id, e);
        }
    }

    @Override
    public Optional<Movie> update(Movie entity) {
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement  = connection.prepareStatement("UPDATE movies SET name = ?, genre = ?, movieDate = ?, movieTime = ? WHERE id = ?");)
        {
            statement.setString(1,entity.getName());
            statement.setString(2,entity.getGenre());
            statement.setDate(3, Date.valueOf(entity.getMovieDate()));
            statement.setTime(4, Time.valueOf(entity.getMovieTime()));
            statement.setLong(5,entity.getId());
            int affectedRows = statement.executeUpdate();
            return affectedRows!=0? Optional.empty():Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error updating movie: " + entity, e);
        }
    }
}
