package cinema.repository;

import cinema.domain.Seat;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class SeatDBRepository implements ISeatRepository{
    protected String url;
    protected String username;
    protected String password;

    public SeatDBRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public Seat findOne(String nr) {
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM seats WHERE nr=?");)
        {
            statement.setString(1, nr);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                long id = result.getLong("id");
                int seatRow = result.getInt("seatRow");
                int seatColumn = result.getInt("seatColumn");
                float price = result.getFloat("price");
                boolean isAvailable = result.getBoolean("isAvailable");
                Seat seat = new Seat(nr, seatRow, seatColumn, price, isAvailable);
                seat.setId(id);
                return seat;
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding seat with nr: " + nr, e);
        }
        return null;
    }

    @Override
    public Seat findOne(Long id) {
        return null;
    }

    @Override
    public Iterable<Seat> findAll() {
        List<Seat> seats = new ArrayList<>();

        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             Statement statement = connection.createStatement();
             ResultSet result = statement.executeQuery("SELECT * FROM seats")) {
            while (result.next()) {
                long id = result.getLong("id");
                String nr = result.getString("nr");
                int seatRow = result.getInt("seatRow");
                int seatColumn = result.getInt("seatColumn");
                float price = result.getFloat("price");
                boolean isAvailable = result.getBoolean("isAvailable");
                Seat seat = new Seat(nr, seatRow, seatColumn, price, isAvailable);
                seat.setId(id);
                seats.add(seat);
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding all seats", e);
        }

        return seats;
    }

    @Override
    public Optional<Seat> save(Seat entity) {
        return Optional.empty();
    }

    @Override
    public Optional<Seat> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<Seat> update(Seat entity) {
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement  = connection.prepareStatement("UPDATE seats SET nr = ?, seatRow = ?, seatColumn = ?, price = ?, isAvailable = ? WHERE id = ?");)
        {
            statement.setString(1,entity.getNr());
            statement.setInt(2, entity.getSeatRow());
            statement.setInt(3, entity.getSeatColumn());
            statement.setFloat(4, entity.getPrice());
            statement.setBoolean(5, entity.isAvailable());
            statement.setLong(6,entity.getId());
            int affectedRows = statement.executeUpdate();
            return affectedRows!=0? Optional.empty():Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error updating seat: " + entity, e);
        }
    }
}
