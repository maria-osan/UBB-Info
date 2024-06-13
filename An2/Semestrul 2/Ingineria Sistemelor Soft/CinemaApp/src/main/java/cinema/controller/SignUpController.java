package cinema.controller;

import cinema.domain.validators.ValidationException;
import cinema.service.Service;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.io.IOException;

public class SignUpController {
    private Service service;

    public void setService(Service service) {
        this.service = service;
    }

    @FXML
    private TextField name;
    @FXML
    private TextField email;
    @FXML
    private TextField username;
    @FXML
    private TextField password;


    @FXML
    public void onCreateAccountButtonClick(ActionEvent actionEvent) {
        try{
            if(email.getText().matches(".*@admin\\..+")) {
                service.handleSignUp(name.getText(), email.getText(), username.getText(), password.getText(), true);

                FXMLLoader stageLoader = new FXMLLoader();
                stageLoader.setLocation(getClass().getResource("/cinema/admin-view.fxml"));
                AnchorPane appLayout = stageLoader.load();

                Stage newStage = new Stage();
                Scene scene = new Scene(appLayout, 450, 450);
                newStage.setTitle("Cinema - account: " + username.getText());
                newStage.setScene(scene);

                AdminController adminController = stageLoader.getController();
                adminController.setService(this.service, service.findByUsername(username.getText()));
                adminController.initApp();

                newStage.show();
            } else {
                service.handleSignUp(name.getText(), email.getText(), username.getText(), password.getText(), false);

                FXMLLoader stageLoader = new FXMLLoader();
                stageLoader.setLocation(getClass().getResource("/cinema/spectator-view.fxml"));
                AnchorPane appLayout = stageLoader.load();

                Stage newStage = new Stage();
                Scene scene = new Scene(appLayout, 600, 400);
                newStage.setTitle("Cinema - account: " + username.getText());
                newStage.setScene(scene);

                SpectatorController spectatorController = stageLoader.getController();
                spectatorController.setService(this.service, service.findByUsername(username.getText()));
                spectatorController.initApp();

                newStage.show();
            }

            name.clear();
            email.clear();
            username.clear();
            password.clear();

        } catch (ValidationException | IOException ex) {
            MessageAlert.showErrorMessage(null, ex.getMessage());
        }
    }

    @FXML
    public void onLogInClick(ActionEvent actionEvent) throws IOException {
        FXMLLoader stageLoader = new FXMLLoader();
        stageLoader.setLocation(getClass().getResource("/cinema/login-view.fxml"));
        AnchorPane logInLayout = stageLoader.load();

        Stage stage = (Stage) ((Node)actionEvent.getSource()).getScene().getWindow();
        Scene scene = new Scene(logInLayout);
        stage.setTitle("Login");
        stage.setScene(scene);

        LoginController loginController = stageLoader.getController();
        loginController.setService(this.service);

        stage.show();
    }
}
