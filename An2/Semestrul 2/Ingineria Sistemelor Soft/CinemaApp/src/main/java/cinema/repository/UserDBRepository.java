package cinema.repository;

import cinema.domain.User;
import cinema.utils.AESUtil;

import java.sql.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

public class UserDBRepository implements IUserRepository{
    protected String url;
    protected String username;
    protected String password;

    public UserDBRepository(String url, String username, String password) {
        this.url = url;
        this.username = username;
        this.password = password;
    }

    @Override
    public User findOne(String username) {
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM users WHERE username=?");)
        {
            statement.setString(1, username);
            ResultSet result = statement.executeQuery();
            if (result.next()) {
                long id = result.getLong("id");
                String name = result.getString("name");
                String email = result.getString("email");
                String encryptedPassword = result.getString("password");
                String password = AESUtil.decrypt(encryptedPassword);
                boolean isAdmin = result.getBoolean("isAdmin");
                User user = new User(name, email, username, password, isAdmin);
                user.setId(id);
                return user;
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding user with username: " + username, e);
        }
        return null;
    }

    @Override
    public User findOne(Long id) {
        return null;
    }

    @Override
    public Iterable<User> findAll() {
        List<User> users = new ArrayList<>();

        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("SELECT * FROM users");
             ResultSet result = statement.executeQuery()) {
            while (result.next()) {
                long id = result.getLong("id");
                String name = result.getString("name");
                String email = result.getString("email");
                String username = result.getString("username");
                String encryptedPassword = result.getString("password");
                String password = AESUtil.decrypt(encryptedPassword);
                boolean isAdmin = result.getBoolean("isAdmin");
                User user = new User(name, email, username, password, isAdmin);
                user.setId(id);
                users.add(user);
            }
        } catch (SQLException e) {
            throw new RuntimeException("Error finding all users", e);
        }

        return users;
    }

    @Override
    public Optional<User> save(User entity) {
        try(Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
            PreparedStatement statement  = connection.prepareStatement("INSERT INTO users(name, email, username, password, isAdmin) VALUES (?,?,?,?,?)");)
        {
            statement.setString(1, entity.getName());
            statement.setString(2, entity.getEmail());
            statement.setString(3, entity.getUsername());
            String encryptedPassword = AESUtil.encrypt(entity.getPassword());
            statement.setString(4, encryptedPassword);
            statement.setBoolean(5, entity.isAdmin());
            int affectedRows = statement.executeUpdate();
            return affectedRows!=0? Optional.empty():Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error saving user: " + entity, e);
        }
    }

    @Override
    public Optional<User> delete(Long aLong) {
        return Optional.empty();
    }

    @Override
    public Optional<User> update(User entity) {
        try (Connection connection = DriverManager.getConnection(this.url, this.username, this.password);
             PreparedStatement statement = connection.prepareStatement("UPDATE users SET name = ?, email = ?, username = ?, password = ?, isAdmin = ? WHERE id = ?")) {
            statement.setString(1, entity.getName());
            statement.setString(2, entity.getEmail());
            statement.setString(3, entity.getUsername());
            String encryptedPassword = AESUtil.encrypt(entity.getPassword());
            statement.setString(4, encryptedPassword);
            statement.setBoolean(5, entity.isAdmin());
            statement.setLong(6, entity.getId());
            int affectedRows = statement.executeUpdate();
            return affectedRows != 0 ? Optional.empty() : Optional.of(entity);
        } catch (SQLException e) {
            throw new RuntimeException("Error updating user: " + entity, e);
        }
    }
}
