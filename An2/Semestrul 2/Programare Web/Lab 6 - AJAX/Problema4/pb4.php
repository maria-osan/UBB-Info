<?php

header("Access-Control-Allow-Origin: *");


function checkIfSolution(): string
{
    global $game;
    $status = "continue";

    if($game[0] == $game[1] && $game[0] == $game[2] && ($game[0] == "X" || $game[0] == "O")) // first row
        $status = $game[0] . " won!";

    else if($game[3] == $game[4] && $game[3] == $game[5] && ($game[3] == "X" || $game[3] == "O")) // second row
        $status = $game[3] . " won!";
    else if($game[6] == $game[7] && $game[6] == $game[8] && ($game[6] == "X" || $game[6] == "O")) // third row
        $status = $game[6] . " won!";

    else if($game[0] == $game[3] && $game[0] == $game[6] && ($game[0] == "X" || $game[0] == "O")) // first column
        $status = $game[0] . " won!";

    else if($game[1] == $game[4] && $game[1] == $game[7] && ($game[1] == "X" || $game[1] == "O")) // second column
        $status = $game[1] . " won!";

    else if($game[2] == $game[5] && $game[2] == $game[8] && ($game[2] == "X" || $game[2] == "O")) // third column
        $status = $game[2] . " won!";

    else if($game[0] == $game[4] && $game[0] == $game[8] && ($game[0] == "X" || $game[0] == "O")) // principal diagonal
        $status = $game[0] . " won!";

    else if($game[2] == $game[4] && $game[2] == $game[6] && ($game[2] == "X" || $game[2] == "O")) // secondary diagonal
        $status = $game[2] . " won!";

    else if(!str_contains($game, "-")) // there is no possible move
        $status = "Tie";

    return $status;
}



$game = $_GET["game"];
$status = checkIfSolution();

if($status == "continue") {
    while(true){
        $i = rand(0, 8);
        if($game[$i] === "-"){
            $game[$i] = "O";
            break;
        }
    }

    $status = checkIfSolution();
}

$response = array("status" => $status, "game" => $game);
echo json_encode($response);

?>
