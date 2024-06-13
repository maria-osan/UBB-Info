package cinema;

import cinema.controller.LoginController;
import cinema.domain.validators.MovieValidator;
import cinema.domain.validators.UserValidator;
import cinema.repository.*;
import cinema.service.Service;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Properties;

public class MainApp extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Properties props = new Properties();
        props.load(new FileInputStream("config.properties"));

        String dbUrl = props.getProperty("db.url");
        String dbUsername = props.getProperty("db.username");
        String dbPassword = props.getProperty("db.password");

        Service service = getService(dbUrl, dbUsername, dbPassword);

        FXMLLoader fxmlLoader = new FXMLLoader(MainApp.class.getResource("/cinema/login-view.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 400, 400);
        stage.setTitle("Login");
        stage.setScene(scene);

        LoginController loginController = fxmlLoader.getController();
        loginController.setService(service);

        stage.show();
    }

    private static Service getService(String dbUrl, String dbUsername, String dbPassword) {
        IUserRepository userRepo = new UserDBRepository(dbUrl, dbUsername, dbPassword);
        ISeatRepository seatRepo = new SeatDBRepository(dbUrl, dbUsername, dbPassword);
        IMovieRepository movieRepo = new MovieDBRepository(dbUrl, dbUsername, dbPassword);
        ITicketRepository ticketRepo = new TicketDBRepository(dbUrl, dbUsername, dbPassword);

        Service service = new Service(userRepo, seatRepo, movieRepo, ticketRepo, new UserValidator(), new MovieValidator());

        // Check and reset seat availability if necessary
        service.checkAndResetSeatAvailability();
        return service;
    }

    public static void main(String[] args) {
        launch();
    }
}