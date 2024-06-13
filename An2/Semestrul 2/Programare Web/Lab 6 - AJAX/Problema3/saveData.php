<?php
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");

// Cream o conexiune la baza de date
$mysqli = new mysqli("localhost", "root", "", "lab6_ajax");

// Verificam conexiunea
if ($mysqli->connect_error) {
    die('Could not connect: ' . $mysqli->connect_error);
}

// Verificăm dacă s-a trimis o cerere POST cu toți parametrii necesari
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Adaugă cod de debugging
    file_put_contents('php://stderr', print_r($_POST, true));

    if (isset($_POST['id']) && isset($_POST['lastname']) && isset($_POST['firstname']) && isset($_POST['phoneNumber']) && isset($_POST['email'])) {
        $id = $_POST['id'];
        $lastname = $_POST['lastname'];
        $firstname = $_POST['firstname'];
        $phoneNumber = $_POST['phoneNumber'];
        $email = $_POST['email'];

        $sql = "UPDATE users SET lastname = ?, firstname = ?, phoneNumber = ?, email = ? WHERE id = ?";
        $stmt = $mysqli->prepare($sql);
        $stmt->bind_param("ssssi", $lastname, $firstname, $phoneNumber, $email, $id);

        // Verificăm dacă actualizarea s-a realizat cu succes
        if ($stmt->execute()) {
            echo json_encode(array("success" => true));
        } else {
            echo json_encode(array("error" => "Failed to update item"));
        }
        $stmt->close();
    } else {
        echo json_encode(array("error" => "Missing parameters"));
    }
} else {
    echo json_encode(array("error" => "Invalid request method"));
}

$mysqli->close();
?>