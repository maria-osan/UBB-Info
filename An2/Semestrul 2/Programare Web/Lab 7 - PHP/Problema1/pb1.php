<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Conectare la baza de date
    $conn = new mysqli("localhost", "root", "", "lab7_php");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    $plecare = htmlspecialchars(trim($_POST['plecare']));
    $sosire = htmlspecialchars(trim($_POST['sosire']));
    $tip_cursa = htmlspecialchars(trim($_POST['tip_cursa']));

    if ($tip_cursa == 'direct') {
        // Căutare curse directe
        $sql = "SELECT * FROM trenuri WHERE localitate_plecare = ? AND localitate_sosire = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $plecare, $sosire);
    } else {
        // Căutare curse cu legături
        $sql = "SELECT t1.nr_tren AS tren1, t1.tip_tren AS tip_tren1, t1.localitate_plecare AS plecare1, t1.localitate_sosire AS legatura, t1.ora_plecare AS ora_plecare1, t1.ora_sosire AS ora_sosire1,
                       t2.nr_tren AS tren2, t2.tip_tren AS tip_tren2, t2.localitate_plecare AS plecare2, t2.localitate_sosire AS sosire2, t2.ora_plecare AS ora_plecare2, t2.ora_sosire AS ora_sosire2
                FROM trenuri t1
                JOIN trenuri t2 ON t1.localitate_sosire = t2.localitate_plecare
                WHERE t1.localitate_plecare = ? AND t2.localitate_sosire = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ss", $plecare, $sosire);
    }

    $stmt->execute();
    $result = $stmt->get_result();
    $output = "";

    if ($result->num_rows > 0) {
        while ($row = $result->fetch_assoc()) {
            if ($tip_cursa == 'direct') {
                $output .= "Tren direct: <br>" . htmlspecialchars($row["nr_tren"]) . " (" . htmlspecialchars($row["tip_tren"]) . ")  " . htmlspecialchars($row["localitate_plecare"]) . " (ora plecare: " . htmlspecialchars($row["ora_plecare"]) . ") - " . htmlspecialchars($row["localitate_sosire"]) . " (ora sosire: " . htmlspecialchars($row["ora_sosire"]) . ")<br>";
            } else {
                $output .= "Tren cu legătură: <br>" . htmlspecialchars($row["tren1"]) . " (" . htmlspecialchars($row["tip_tren1"]) . ") " . htmlspecialchars($row["plecare1"]) . " (ora plecare: " . htmlspecialchars($row["ora_plecare1"]) . ") - " . htmlspecialchars($row["legatura"]) . " (ora sosire: " . htmlspecialchars($row["ora_sosire1"]) . ") <br> " .
                    htmlspecialchars($row["tren2"]) . " (" . htmlspecialchars($row["tip_tren2"]) . ") " . htmlspecialchars($row["plecare2"]) . " (ora plecare: " . htmlspecialchars($row["ora_plecare2"]) . ") - " . htmlspecialchars($row["sosire2"]) . " (ora sosire: " . htmlspecialchars($row["ora_sosire2"]) . ")<br>";
            }
        }
    } else {
        $output = "Nu s-au găsit trenuri.";
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
    <title>Rezultate Căutare Trenuri</title>
</head>

<body>
    <form method="post" action="http://localhost/Lab7PHP/Problema1/pb1.php">
        <label for="plecare">Localitate Plecare:</label>
        <input type="text" id="plecare" name="plecare" required><br><br>
        
        <label for="sosire">Localitate Sosire:</label>
        <input type="text" id="sosire" name="sosire" required><br><br>
        
        <input type="radio" id="curse_directe" name="tip_cursa" value="direct" required>
        <label for="curse_directe">Curse directe</label>

        <input type="radio" id="curse_legatura" name="tip_cursa" value="legatura" required>
        <label for="curse_legatura">Curse cu legatura</label><br><br>
        
        <input type="submit" value="Cauta"><br><br>
    </form>

    <div id="rezultat">
        <?php
        if (isset($output)) {
            echo $output;
        }
        ?>
    </div>
</body>
</html>