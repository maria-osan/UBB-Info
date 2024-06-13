package cinema.repository;

import cinema.domain.Seat;
import cinema.domain.Ticket;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class TicketDBRepository implements ITicketRepository {
    protected String url;
    protected String username;
    protected String password;

    public TicketDBRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Ticket findOne(Long id) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM tickets WHERE id = ?")) {
            statement.setLong(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                String buyerName = resultSet.getString("buyerName");
                long movieId = resultSet.getLong("movieId");
                float price = resultSet.getFloat("price");
                String seatsString = resultSet.getString("seats");
                List<Seat> seats = parseSeats(seatsString);
                Ticket ticket = new Ticket(buyerName, movieId, price, seats);
                ticket.setId(id);
                return ticket;
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding ticket with id: " + id, e);
        }
        return null;
    }

    @Override
    public Iterable<Ticket> findAll() {
        List<Ticket> tickets = new ArrayList<>();

        try (Connection connection = DriverManager.getConnection(url, username, password);
             Statement statement = connection.createStatement();
             ResultSet resultSet = statement.executeQuery("SELECT * FROM tickets")) {
            while (resultSet.next()) {
                long id = resultSet.getLong("id");
                String buyerName = resultSet.getString("buyerName");
                long movieId = resultSet.getLong("movieId");
                float price = resultSet.getFloat("price");
                String seatsString = resultSet.getString("seats");
                List<Seat> seats = parseSeats(seatsString);
                Ticket ticket = new Ticket(buyerName, movieId, price, seats);
                ticket.setId(id);
                tickets.add(ticket);
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding all tickets", e);
        }

        return tickets;
    }

    @Override
    public Optional<Ticket> save(Ticket entity) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("INSERT INTO tickets (buyerName, movieId, price, seats) VALUES (?, ?, ?, ?)")) {
            statement.setString(1, entity.getBuyerName());
            statement.setLong(2, entity.getIdMovie());
            statement.setFloat(3, entity.getPrice());
            statement.setString(4, seatsToString(entity.getSeats()));  // Convert seats to string
            int affectedRows = statement.executeUpdate();
            return affectedRows != 0 ? Optional.empty() : Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error saving ticket: " + entity, e);
        }
    }

    @Override
    public Optional<Ticket> delete(Long id) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("DELETE FROM tickets WHERE id = ?")) {
            Optional<Ticket> ticket = Optional.ofNullable(findOne(id));
            statement.setLong(1, id);
            int affectedRows = statement.executeUpdate();
            return affectedRows == 0 ? Optional.empty() : ticket;
        } catch (SQLException e) {
            throw new RuntimeException("Error deleting ticket with id: " + id, e);
        }
    }

    @Override
    public Optional<Ticket> update(Ticket entity) {
        try (Connection connection = DriverManager.getConnection(url, username, password);
             PreparedStatement statement = connection.prepareStatement("UPDATE tickets SET buyerName = ?, movieId = ?, price = ?, seats = ? WHERE id = ?")) {
            statement.setString(1, entity.getBuyerName());
            statement.setLong(2, entity.getIdMovie());
            statement.setFloat(3, entity.getPrice());
            statement.setString(4, seatsToString(entity.getSeats()));  // Convert seats to string
            statement.setLong(5, entity.getId());
            int affectedRows = statement.executeUpdate();
            return affectedRows != 0 ? Optional.empty() : Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error updating ticket: " + entity, e);
        }
    }

    private List<Seat> parseSeats(String seatsStr) {
        SeatDBRepository seatRepo = new SeatDBRepository(url, username, password);

        if (seatsStr == null || seatsStr.isEmpty()) {
            return new ArrayList<>();
        }

        // seat numbers are comma-separated
        String[] seatNumbers = seatsStr.split(",");
        List<Seat> seats = new ArrayList<>();
        for (String seatNumber : seatNumbers) {
            Seat seat = seatRepo.findOne(seatNumber);
            if (seat != null) {
                seats.add(seat);
            }
        }
        return seats;
    }

    private String seatsToString(List<Seat> seats) {
        // Convert the list of Seat objects to a comma-separated string of seat numbers
        StringBuilder seatsStr = new StringBuilder();
        for (Seat seat : seats) {
            if (!seatsStr.isEmpty()) {
                seatsStr.append(",");
            }
            seatsStr.append(seat.getNr());
        }
        return seatsStr.toString();
    }
}
