let rows = 4;
let cols = 4;
let numbers = [];
let emptyCell = { row: 0, col: 0 };

// Function to change the size of the puzzle based on user selection
function changePuzzleSize() {
    const size = document.getElementById("size").value;
    const dimensions = size.split("x");
    rows = parseInt(dimensions[0]);
    cols = parseInt(dimensions[1]);
    createPuzzle();
}

// Function to create the puzzle table
function createPuzzle() {
    const totalCells = rows * cols;
    let puzzleTable = document.getElementById("puzzle");
    let counter = 1;

    puzzleTable.innerHTML = ""; // Clear existing table

    // Create rows and columns for the table
    for (let i = 0; i < rows; i++) {
        let row = puzzleTable.insertRow();
        for (let j = 0; j < cols; j++) {
            let cell = row.insertCell();
            if (counter < totalCells) {
                cell.textContent = counter; // Fill cells with numbers
                numbers.push(counter); // Store numbers for shuffling
            } else {
                cell.textContent = ""; // Empty the last cell
                emptyCell = { row: i, col: j }; // Store empty cell position
            }
            // Add click event listener to each cell
            cell.addEventListener("click", () => {
                if (isValidMove(i, j)) {
                    moveCell(i, j);
                }
            });
            counter++;
        }
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
    let puzzleTable = document.getElementById("puzzle");
    const totalCells = rows * cols;
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            let cell = puzzleTable.rows[i].cells[j];
            if (index < totalCells - 1) {
                cell.textContent = numbers[index]; // Fill cells with shuffled numbers
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
    let puzzleTable = document.getElementById("puzzle");
    puzzleTable.rows[emptyCell.row].cells[emptyCell.col].textContent = puzzleTable.rows[row].cells[col].textContent;
    puzzleTable.rows[row].cells[col].textContent = "";
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
window.onload = createPuzzle;

// Add event listener for arrow key presses to move cells
document.addEventListener("keydown", handleArrowKeyPress);