<?php
header('Content-Type: application/json');

$conn = new mysqli("localhost", "root", "", "lab6_ajax");

if ($conn->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $conn->connect_error]));
}

if (isset($_GET['id'])) {
    $id = intval($_GET['id']);
    $sql = "SELECT lastname, firstname, phoneNumber, email FROM users WHERE id = $id";
    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        $data = $result->fetch_assoc();
        echo json_encode($data);
    } else {
        echo json_encode(["error" => "No data found for the specified ID"]);
    }
} else {
    echo json_encode(["error" => "ID parameter is missing"]);
}

$conn->close();
?>