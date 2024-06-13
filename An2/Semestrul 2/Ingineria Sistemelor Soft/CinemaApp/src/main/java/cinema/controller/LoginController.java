package cinema.controller;

import cinema.domain.validators.ValidationException;
import cinema.service.Service;
import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Node;
import javafx.scene.Scene;
import javafx.scene.control.PasswordField;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.Stage;

import java.io.IOException;

public class LoginController {
    private Service service;

    public void setService(Service service) {
        this.service = service;
    }

    @FXML
    private TextField username;
    @FXML
    private PasswordField password;

    @FXML
    public void onLogInButtonClick(ActionEvent actionEvent) {
        try{
            String u = username.getText();
            String p = password.getText();
            boolean isAdmin = service.handleLogin(u, p);

            if(isAdmin) {
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
                username.clear();
                password.clear();

                //((Node)(actionEvent.getSource())).getScene().getWindow().hide();
            } else {
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
                username.clear();
                password.clear();

                //((Node)(actionEvent.getSource())).getScene().getWindow().hide();
            }
        } catch (ValidationException | IOException ex) {
            MessageAlert.showErrorMessage(null, ex.getMessage());
        }
    }

    @FXML
    public void onSingUpClick(ActionEvent actionEvent) throws IOException {
        FXMLLoader stageLoader = new FXMLLoader();
        stageLoader.setLocation(getClass().getResource("/cinema/signup-view.fxml"));
        AnchorPane signUpLayout = stageLoader.load();

        Stage stage = (Stage) ((Node)actionEvent.getSource()).getScene().getWindow();
        Scene scene = new Scene(signUpLayout);
        stage.setTitle("SignUp");
        stage.setScene(scene);

        SignUpController signUpController = stageLoader.getController();
        signUpController.setService(this.service);

        stage.show();
    }
}
