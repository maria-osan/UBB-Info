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
$userId = $_SESSION['userId'];

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['image'])) {
    $upload_dir = 'images/';
    $filename = uploadImage($_FILES['image'], $upload_dir);
    if ($filename) {
        $sql = "INSERT INTO images (userId, filename) VALUES (?, ?)";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("is", $userId, $filename);
        $stmt->execute();
        $stmt->close();
        echo "Image uploaded successfully.";
    } else {
        echo "Error uploading image.";
    }
}

$sql = "SELECT * FROM images WHERE userId = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $userId);
$stmt->execute();
$result = $stmt->get_result();

?>

<!DOCTYPE html>
<html>
<head>
    <title>Profile</title>
</head>

<body>
    <h2>Welcome to your profile, <?php echo htmlspecialchars($_SESSION['userName']); ?></h2>
    <form method="POST" action="" enctype="multipart/form-data">
        <input type="file" name="image" required>
        <input type="submit" value="Upload Image">
    </form>
    <h3>Your Images:</h3>
    <?php while ($row = $result->fetch_assoc()) : ?>
        <div>
            <br><img src="images/<?php echo htmlspecialchars($row['filename']); ?>" width="200" height="200">
            <br><form method="POST" action="deleteImage.php">
                <input type="hidden" name="imageId" value="<?php echo $row['id']; ?>">
                <input type="hidden" name="filename" value="<?php echo $row['filename']; ?>">
                <input type="submit" value="Delete">
            </form><br>
        </div>
    <?php endwhile; ?>
    <h3>Other Users:</h3>
    <?php
    $sql = "SELECT id, name FROM users WHERE id != ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $userId);
    $stmt->execute();
    $result = $stmt->get_result();
    while ($row = $result->fetch_assoc()) :
    ?>
        <li>
            <a href="viewProfile.php?userId=<?php echo $row['id']; ?>"><?php echo htmlspecialchars($row['name']); ?></a>
        </li>
    <?php endwhile; ?>
    <br><br><button><a href="logout.php">Logout</a></button>
</body>
</html>

<?php
$stmt->close();
$conn->close();
?>