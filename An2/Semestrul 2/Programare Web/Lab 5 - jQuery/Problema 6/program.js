let rows = 4;
let cols = 4;
let numbers = [];
let emptyCell = { row: 0, col: 0 };

// Function to change the size of the puzzle based on user selection
function changePuzzleSize() {
    const size = $("#size").val();
    const dimensions = size.split("x");
    rows = parseInt(dimensions[0]);
    cols = parseInt(dimensions[1]);
    createPuzzle();
}

// Function to create the puzzle table
function createPuzzle() {
    const totalCells = rows * cols;
    let puzzleTable = $("#puzzle");
    let counter = 1;

    puzzleTable.empty(); // Clear existing table

    // Create rows and columns for the table
    for (let i = 0; i < rows; i++) {
        let row = $("<tr></tr>");
        for (let j = 0; j < cols; j++) {
            let cell = $("<td></td>");
            if (counter < totalCells) {
                cell.text(counter); // Fill cells with numbers
                numbers.push(counter); // Store numbers for shuffling
            } else {
                cell.text(""); // Empty the last cell
                emptyCell = { row: i, col: j }; // Store empty cell position
            }
            // Add click event listener to each cell
            cell.on("click", () => {
                if (isValidMove(i, j)) {
                    moveCell(i, j);
                }
            });
            row.append(cell);
            counter++;
        }
        puzzleTable.append(row);
    }
    shuffleNumbers(); // Shuffle numbers before displaying the puzzle
}

// Function to shuffle numbers
function shuffleNumbers() {
    numbers = [];
    const totalCells = rows * cols;
    for (let i = 1; i < totalCells; i++) {
        numbers.push(i);
    }
    numbers.sort(() => Math.random() - 0.5); // Shuffle the numbers array
    fillPuzzle();
}

// Function to fill the puzzle table with shuffled numbers
function fillPuzzle() {
    let index = 0;
    let puzzleTable = $("#puzzle");
    const totalCells = rows * cols;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            let cell = puzzleTable.find("tr").eq(i).find("td").eq(j);
            if (index < totalCells - 1) {
                cell.text(numbers[index]); // Fill cells with shuffled numbers
            }
            index++;
        }
    }
}

// Function to check if a move is valid
function isValidMove(row, col) {
    return Math.abs(row - emptyCell.row) + Math.abs(col - emptyCell.col) === 1;
}

// Function to move a cell into the empty cell position
function moveCell(row, col) {
    let puzzleTable = $("#puzzle");
    puzzleTable.find("tr").eq(emptyCell.row).find("td").eq(emptyCell.col).text(puzzleTable.find("tr").eq(row).find("td").eq(col).text());
    puzzleTable.find("tr").eq(row).find("td").eq(col).text("");
    emptyCell.row = row;
    emptyCell.col = col;
}

// Function to handle arrow key presses for moving cells
function handleArrowKeyPress(event) {
    switch (event.key) {
        case "ArrowUp":
            if (isValidMove(emptyCell.row + 1, emptyCell.col)) {
                moveCell(emptyCell.row + 1, emptyCell.col);
            }
            break;
        case "ArrowDown":
            if (isValidMove(emptyCell.row - 1, emptyCell.col)) {
                moveCell(emptyCell.row - 1, emptyCell.col);
            }
            break;
        case "ArrowLeft":
            if (isValidMove(emptyCell.row, emptyCell.col + 1)) {
                moveCell(emptyCell.row, emptyCell.col + 1);
            }
            break;
        case "ArrowRight":
            if (isValidMove(emptyCell.row, emptyCell.col - 1)) {
                moveCell(emptyCell.row, emptyCell.col - 1);
            }
            break;
    }
}

// Call createPuzzle function when the window loads
$(document).ready(function() {
    createPuzzle();
});

// Add event listener for arrow key presses to move cells
$(document).keydown(handleArrowKeyPress);