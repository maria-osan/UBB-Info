<?php

session_start();
if (!isset($_SESSION['userId'])) {
    header("Location: login.php");
    exit();
}
require_once 'includes/db.php';
require_once 'includes/functions.php';

$db = new Database();
$conn = $db->getConnection();

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['imageId']) && isset($_POST['filename'])) {
    $imageId = $_POST['imageId'];
    $filename = $_POST['filename'];

    // Verifică dacă utilizatorul are dreptul de a șterge această imagine
    $sql = "SELECT * FROM images WHERE id = ? AND userId = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("ii", $imageId, $_SESSION['userId']);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        // Șterge imaginea din baza de date
        $sql = "DELETE FROM images WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("i", $imageId);
        $stmt->execute();
        $stmt->close();

        // Șterge fișierul din sistemul de fișiere
        $filepath = 'images/' . $filename;
        if (file_exists($filepath)) {
            unlink($filepath);
        }

        echo "Image deleted successfully.";
    } else {
        echo "You do not have permission to delete this image.";
    }
}

$conn->close();
header("Location: profile.php");
exit();

?>