<?php
session_start();
if (!isset($_SESSION['userId'])) {
    header("Location: login.php");
    exit();
}
if (!isset($_GET['userId'])) {
    header("Location: profile.php");
    exit();
}

require_once 'includes/db.php';
require_once 'includes/functions.php';

$db = new Database();
$conn = $db->getConnection();
$viewUserId = $_GET['userId'];

// Obține informațiile despre utilizator
$sql = "SELECT name FROM users WHERE id = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $viewUserId);
$stmt->execute();
$result = $stmt->get_result();
if ($result->num_rows != 1) {
    header("Location: profile.php");
    exit();
}
$user = $result->fetch_assoc();

// Obține imaginile utilizatorului
$sql = "SELECT * FROM images WHERE userId = ?";
$stmt = $conn->prepare($sql);
$stmt->bind_param("i", $viewUserId);
$stmt->execute();
$images = $stmt->get_result();
?>
<!DOCTYPE html>
<html>
<head>
    <title>Profile of <?php echo htmlspecialchars($user['name']); ?></title>
</head>
<body>
    <h2>Profile of <?php echo htmlspecialchars($user['name']); ?></h2>
    <h3>Images:</h3>
    <?php while ($row = $images->fetch_assoc()) : ?>
        <div>
            <img src="images/<?php echo htmlspecialchars($row['filename']); ?>" width="200" height="200">
        </div>
    <?php endwhile; ?>
    <br><button><a href="profile.php">Back to your profile</a></button>
</body>
</html>
<?php
$stmt->close();
$conn->close();
?>