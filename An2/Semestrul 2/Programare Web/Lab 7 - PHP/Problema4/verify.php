<?php

// Database connection
$conn = new mysqli("localhost","root", "", "lab7_php");

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process verification token
if (isset($_GET['token'])) {
    $token = $_GET['token'];

    // Update user record in database to mark email as verified
    $sql = "UPDATE users SET verified = 1 WHERE token = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $token);

    if ($stmt->execute()) {
        echo "Email verification successful. You can now login to your account.";
    } else {
        echo "Email verification failed.";
    }

    $stmt->close();
    $conn->close();
} else {
    echo "Invalid verification token.";
}

?>