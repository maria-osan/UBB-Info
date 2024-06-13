<?php

ini_set('display_errors', 1);
error_reporting(E_ALL);

// Database connection
$conn = new mysqli("localhost","root", "", "lab7_php");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Process registration form
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
    $verified = 0;
    $token = bin2hex(random_bytes(16)); // Generate verification token

    // Insert user data into database
    $sql = "INSERT INTO users (name, email, password, verified, token) VALUES (?, ?, ?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sssis", $name, $email, $password, $verified, $token);

    if ($stmt->execute()) {
        // Send verification email
        $to = $email;
        $subject = "Verify your email address";
        $message = "Click the following link to verify your email address: http://localhost/Lab7PHP/Problema4/verify.php?token=$token";
        $headers = "From: you@localhost" . "\r\n" .
                   "Reply-To: $email" . "\r\n" .
                   "X-Mailer: PHP/" . phpversion();

        if (mail($to, $subject, $message, $headers)) {
           echo "Registration successful. Please check your email to verify your account.";
        } else {
            echo "Registration successful, but failed to send verification email.";
        }
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }

    $stmt->close();
    $conn->close();
}

?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Register</title>
</head>

<body>
    <h2>Create your account</h2>

    <form method="POST" action="http://localhost/Lab7PHP/Problema4/register.php">
        <label for="name">Nume: </label><br>
        <input type="text" id="name" name="name" required autocomplete="off"><br><br>

        <label for="email">Email: </label><br>
        <input type="email" id="email" name="email" required autocomplete="off"><br><br>

        <label for="password">Parola: </label><br>
        <input type="password" id="password" name="password" required autocomplete="off"><br><br>

        <input type="submit" value="Register">
    </form>
</body>
</html>