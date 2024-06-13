package cinema.controller;

import cinema.domain.Movie;
import cinema.domain.Seat;
import cinema.domain.User;
import cinema.service.Service;
import cinema.utils.Observer;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.Alert;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.AnchorPane;

import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SpectatorController implements Observer {
    private Service service;
    private User user;

    public void setService(Service service, User user) {
        this.service = service;
        this.user = user;
        service.addObserver(this);  // Register as an observer
        service.checkAndResetSeatAvailability();
        initApp();
    }

    @Override
    public void update() {
        // Update the UI when notified of changes
        refreshSeatStatus();
    }

    private final List<Label> selectedSeats = new ArrayList<>();  // List to store selected labels
    private final Map<String, Label> seatLabels = new HashMap<>();  // Store seat labels by ID

    @FXML
    private Label dateField;
    @FXML
    private Label timeField;
    @FXML
    private Label movieNameField;
    @FXML
    private Label genreField;

    @FXML
    private AnchorPane anchorPane;

    public void initApp() {
        // Set the movie
        Movie todayMovie = service.getTodayMovie();
        movieNameField.setText(todayMovie.getName());
        dateField.setText(todayMovie.getMovieDate().format(DateTimeFormatter.ofPattern("dd.MM.yyyy")));
        genreField.setText(todayMovie.getGenre());
        timeField.setText(todayMovie.getMovieTime().format(DateTimeFormatter.ofPattern("HH:mm")));

        // Initialize seat labels
        initializeSeatLabels();
        refreshSeatStatus();
    }

    private void initializeSeatLabels() {
        for (int i = 1; i <= 6; i++) {
            for(int j = 1; j <= 7; j++) {
                String labelId = "nr" + i + j;
                Label seatLabel = (Label) anchorPane.lookup("#" + labelId);
                if (seatLabel != null) {
                    seatLabels.put(seatLabel.getId(), seatLabel);
                    seatLabel.setStyle("-fx-background-color: grey;");
                }
            }
        }
    }

    private void refreshSeatStatus() {
        // Get the latest seat information and update the seat labels
        for (Seat seat : service.getAllSeats()) {
            Label seatLabel = seatLabels.get(seat.getNr());
            if (seatLabel != null) {
                if (seat.isAvailable()) {
                    seatLabel.setStyle("-fx-background-color: grey;");
                } else {
                    seatLabel.setStyle("-fx-background-color: red;");
                }
            }
        }
    }

    @FXML
    public void onMouseClickSelect(MouseEvent event) {
        Label selectedLabel = (Label) event.getSource();

        if(!selectedSeats.contains(selectedLabel)) {
            // Select the label
            selectedLabel.setStyle("-fx-background-color: limegreen;");
            selectedSeats.add(selectedLabel);
            Seat seat = service.findSeatByNr(selectedLabel.getId());
            String displayText = "Seat: " + seat.getNr() + " - row: " + seat.getSeatRow() + ", column: " +
                    seat.getSeatColumn() + ", price: " + seat.getPrice();
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Seat information", displayText);
        } else {
            // Deselect the label
            selectedLabel.setStyle("-fx-background-color: grey;");
            selectedSeats.remove(selectedLabel);
        }
    }

    @FXML
    public void onPressReserveSeats() {
        try {
            // Get the selected seats
            List<Seat> seats = new ArrayList<>();
            for (Label label : selectedSeats) {
                Seat seat = service.findSeatByNr(label.getId());
                seats.add(seat);
            }

            // Reserve the selected seats
            float totalPrice = service.handleReservation(user, seats);

            // Show success message
            MessageAlert.showMessage(null, Alert.AlertType.INFORMATION, "Reservation successful",
                    "Seats reserved successfully!\nTotal price: " + totalPrice);

            // Clear the selected seats list and reset label styles
            clearSelectedSeats();
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    // Method to clear selected seats and reset label styles
    private void clearSelectedSeats() {
        for (Label label : selectedSeats) {
            label.setStyle("-fx-background-color: red;");
        }
        selectedSeats.clear();
        refreshSeatStatus();
    }

    @FXML
    public void onPressLogout(ActionEvent actionEvent) {
        service.handleLogout(user);
        service.removeObserver(this);
        ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
    }
}
