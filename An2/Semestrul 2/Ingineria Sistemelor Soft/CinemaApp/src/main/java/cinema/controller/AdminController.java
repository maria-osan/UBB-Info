package cinema.controller;

import cinema.domain.Movie;
import cinema.domain.User;
import cinema.service.Service;
import cinema.utils.Observer;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.scene.Node;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

public class AdminController implements Observer {
    private Service service;
    private User user;

    public void setService(Service service, User user) {
        this.service = service;
        this.user = user;
        service.addObserver(this);  // Register as an observer
        initApp();
    }

    @Override
    public void update() {
        // Update the UI when notified of changes
        initApp();
    }

    ObservableList<Movie> moviesObs = FXCollections.observableArrayList();

    @FXML
    private TableView<Movie> moviesTable;
    @FXML
    private TableColumn<Movie, String> movieNameColumn;
    @FXML
    private TableColumn<Movie, String> movieGenreColumn;
    @FXML
    private TableColumn<Movie, LocalDate> movieDateColumn;
    @FXML
    private TableColumn<Movie, LocalTime> movieTimeColumn;

    @FXML
    private TextField movieNameField;
    @FXML
    private TextField movieGenreField;
    @FXML
    private TextField movieDateField;
    @FXML
    private TextField movieTimeField;

    public void initApp() {
        moviesObs.setAll(StreamSupport.stream(service.getAllMovies().spliterator(), false).collect(Collectors.toList()));
        moviesTable.setItems(moviesObs);  // Refresh the table
    }

    @FXML
    public void initialize() {
        moviesTable.setItems(moviesObs);

        movieNameColumn.setCellValueFactory(new PropertyValueFactory<>("name"));
        movieGenreColumn.setCellValueFactory(new PropertyValueFactory<>("genre"));
        movieDateColumn.setCellValueFactory(new PropertyValueFactory<>("movieDate"));
        movieTimeColumn.setCellValueFactory(new PropertyValueFactory<>("movieTime"));
    }

    private void clearTextFields() {
        movieNameField.clear();
        movieGenreField.clear();
        movieDateField.clear();
        movieTimeField.clear();
    }

    @FXML
    public void onPressAddMovie() {
        try{
            String name = movieNameField.getText();
            String genre = movieGenreField.getText();
            String date = movieDateField.getText();
            LocalDate movieDate = parseStringToLocalDate(date);
            String time = movieTimeField.getText();
            LocalTime movieTim = parseStringToLocalTime(time);

            Movie newMovie = new Movie(name, genre, movieDate, movieTim);
            service.addMovie(newMovie);

            initApp();
            clearTextFields();
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressUpdateMovie() {
        try {
            Movie selectedMovie = moviesTable.getSelectionModel().getSelectedItem();

            if(selectedMovie != null) {
                boolean hasUpdates = false;

                if(!movieNameField.getText().isEmpty()) {
                    selectedMovie.setName(movieNameField.getText());
                    hasUpdates = true;
                }
                if(!movieGenreField.getText().isEmpty()) {
                    selectedMovie.setGenre(movieGenreField.getText());
                    hasUpdates = true;
                }
                if(!movieDateField.getText().isEmpty()) {
                    LocalDate movieDate = parseStringToLocalDate(movieDateField.getText());
                    selectedMovie.setMovieDate(movieDate);
                    hasUpdates = true;
                }
                if(!movieTimeField.getText().isEmpty()) {
                    LocalTime movieTime = parseStringToLocalTime(movieTimeField.getText());
                    selectedMovie.setMovieTime(movieTime);
                    hasUpdates = true;
                }

                if(hasUpdates) {
                    service.updateMovie(selectedMovie);
                    initApp();
                    clearTextFields();
                } else {
                    MessageAlert.showErrorMessage(null, "No update provided");
                }
            } else {
                MessageAlert.showErrorMessage(null, "No movie selected");
            }
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    @FXML
    public void onPressDeleteMovie() {
        try {
            Movie selectedMovie = moviesTable.getSelectionModel().getSelectedItem();

            if(selectedMovie != null) {
                service.deleteMovie(selectedMovie.getId());
                initApp();
            } else {
                MessageAlert.showErrorMessage(null, "No movie selected");
            }
        } catch (Exception e) {
            MessageAlert.showErrorMessage(null, e.getMessage());
        }
    }

    private static LocalDate parseStringToLocalDate(String str) {
        String[] parts = str.split("\\.");
        return LocalDate.of(Integer.parseInt(parts[2]), Integer.parseInt(parts[1]), Integer.parseInt(parts[0]));
    }

    private static LocalTime parseStringToLocalTime(String str) {
        String[] parts = str.split(":");
        return LocalTime.of(Integer.parseInt(parts[0]), Integer.parseInt(parts[1]));
    }

    @FXML
    public void onPressLogout(ActionEvent actionEvent) {
        service.handleLogout(user);
        service.removeObserver(this);
        ((Node)(actionEvent.getSource())).getScene().getWindow().hide();
    }
}
