module cinema {
    requires javafx.controls;
    requires javafx.fxml;
    requires java.base;
    requires java.sql;

    opens cinema to javafx.fxml;
    exports cinema;
    exports cinema.domain;
    exports cinema.controller;
    opens cinema.controller to javafx.fxml;
    opens cinema.domain to java.base, javafx.fxml;
}