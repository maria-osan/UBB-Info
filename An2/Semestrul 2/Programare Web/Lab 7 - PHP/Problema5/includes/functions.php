<?php

require_once 'db.php';

function uploadImage($file, $upload_dir) {
    $target_file = $upload_dir . basename($file["name"]);
    $imageFileType = strtolower(pathinfo($target_file, PATHINFO_EXTENSION));
    $check = getimagesize($file["tmp_name"]);
    if ($check !== false) {
        if (move_uploaded_file($file["tmp_name"], $target_file)) {
            return basename($target_file);
        } else {
            return false;
        }
    } else {
        return false;
    }
}

function deleteImage($image_id, $filename) {
    $upload_dir = 'images/';
    $target_file = $upload_dir . $filename;
    if (file_exists($target_file)) {
        unlink($target_file);
    }
    $db = new Database();
    $conn = $db->getConnection();
    $sql = "DELETE FROM images WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("i", $image_id);
    $stmt->execute();
    $stmt->close();
    $conn->close();
}

?>