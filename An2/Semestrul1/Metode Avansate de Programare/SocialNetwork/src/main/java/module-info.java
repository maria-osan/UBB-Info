module com.example.lab10_2 {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.sql;

    opens com.example.lab10_2 to javafx.fxml;
    exports com.example.lab10_2;
    exports com.example.lab10_2.controller;
    opens com.example.lab10_2.controller to javafx.fxml;
    opens com.example.lab10_2.domain to javafx.base;
}