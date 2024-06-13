<?php

header("Access-Control-Allow-Origin: *");

// Establishing a connection to the database
$mysqli = new mysqli("localhost", "root", "", "lab6_ajax");

// Check the connection
if ($mysqli->connect_error) {
	die('Could not connect: ' . $mysqli->connect_error);
}

$sql = "SELECT DISTINCT departure FROM routes";
$stmt = $mysqli->prepare($sql);
$stmt->execute();
$stmt->store_result();
$stmt->bind_result($result);

if($stmt) {
	echo "<option>Select Departure Station</option>";
	
	while($stmt->fetch()){
		echo "<option value=" . $result . ">" . $result . "</option>";
	}
}

$stmt->close();
// Close connection
$mysqli->close();

?>