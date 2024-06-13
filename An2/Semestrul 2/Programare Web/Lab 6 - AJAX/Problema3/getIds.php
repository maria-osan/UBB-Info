<?php
header('Content-Type: application/json');

$conn = new mysqli("localhost", "root", "", "lab6_ajax");

if ($conn->connect_error) {
    die(json_encode(["error" => "Connection failed: " . $conn->connect_error]));
}

$sql = "SELECT id FROM users";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    $ids = [];
    while ($row = $result->fetch_assoc()) {
        $ids[] = $row['id'];
    }
    echo json_encode($ids);
} else {
    echo json_encode([]);
}

$conn->close();
?>