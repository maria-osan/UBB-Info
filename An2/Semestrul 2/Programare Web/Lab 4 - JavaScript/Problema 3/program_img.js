var numbers = []; // Stores the numbers currently flipped
var tile_ids = []; // Stores the IDs of the tiles flipped
var flipped = 0; // Counts the number of flipped pairs

var pairs = [
    "https://cdn-icons-png.freepik.com/512/3132/3132693.png",
    "https://cdn-icons-png.flaticon.com/512/3075/3075977.png",
    "https://cdn-icons-png.flaticon.com/512/2821/2821808.png",
    "https://cdn-icons-png.flaticon.com/512/3014/3014488.png",
    "https://cdn-icons-png.freepik.com/512/3372/3372531.png",
    "https://cdn-icons-png.flaticon.com/512/4062/4062916.png",
    "https://cdn-icons-png.freepik.com/512/6981/6981369.png",
    "https://cdn-icons-png.flaticon.com/512/2821/2821785.png"
];
// Duplicate each image URL in the pairs array
pairs = pairs.flatMap(imageUrl => [imageUrl, imageUrl]);

var flipCount = 0; // Variable to store the number of flips

// Shuffle function to randomly shuffle the pairs array
Array.prototype.shuffle = function() 
{
    var i = this.length,
        j, aux;
    while (--i > 0) 
    {
        j = Math.floor(Math.random() * (i + 1));
        aux = this[i];
        this[i] = this[j];
        this[j] = aux;
    }
}

// Function to flip a tile when clicked
function flip_tile(tile, val) 
{
    if (tile.innerHTML == "" && numbers.length < 2) 
    {
        tile.style.background = '#f0f4f9'; // Changed to white background

        // Get the img element within the tile
        var img = document.createElement('img');
        img.src = val;
        img.alt = 'Image';

        // Append the img element to the tile
        tile.appendChild(img);

        if (numbers.length == 0) // it's the first tile flipped
        {
            numbers.push(val);
            tile_ids.push(tile.id);
        } 
        else if (numbers.length == 1) // it's the second tile flipped
        {
            flipCount++; // Increment flip count

            // Update the DOM to display the flip count
            document.getElementById('flip-count').textContent = "Flips: " + flipCount;

            numbers.push(val);
            tile_ids.push(tile.id);
            if (numbers[0] == numbers[1]) // the two flipped tiles match
            {
                flipped += 2;
                numbers = [];
                tile_ids = [];
                if (flipped == pairs.length) // all pairs are flipped
                {
                    setTimeout(function() 
                    {
                        alert("Congratulations! You've finished the game!");
                        document.getElementById('game-board').innerHTML = "";
                        createGameBoard();
                    }, 1200);
                }
            } 
            else // the two flipped tiles don't match
            {
                // Function to reset the tiles after a delay
                function resetTiles() 
                {
                    var tile_1 = document.getElementById(tile_ids[0]);
                    var tile_2 = document.getElementById(tile_ids[1]);
                    tile_1.style.background = '#d4dfed'; // Reset background color
                    tile_1.innerHTML = "";
                    tile_2.style.background = '#d4dfed'; // Reset background color
                    tile_2.innerHTML = "";
                    numbers = [];
                    tile_ids = [];
                }
                setTimeout(resetTiles, 700);
            }
        }
    }
}

// Function to create the game board
function createGameBoard() 
{
    flipped = 0;
    var output = ''; // Initialize the output variable to store the HTML content of the game board

    var flipCount = 0;
    document.getElementById('flip-count').textContent = "Flips: " + flipCount;

    pairs.shuffle();
    for (var i = 0; i < pairs.length; i++) 
    {
        //output += '<div id="tile_' + i + '" onclick="flip_tile(this, \'' + pairs[i] + '\')" class="tile"><img src="' + pairs[i] + '" alt="Image"></div>';
        output += '<div id="tile_' + i + '" onclick="flip_tile(this, \'' + pairs[i] + '\')" class="tile"></div>';
    }
    document.getElementById('game-board').innerHTML = output;
}

createGameBoard();