$(document).ready(function() {
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

    // Shuffle function to randomly shuffle the array
    function shuffleArray(array) {
        for (var i = array.length - 1; i > 0; i--) {
            var j = Math.floor(Math.random() * (i + 1));
            var temp = array[i];
            array[i] = array[j];
            array[j] = temp;
        }
        return array;
    }

    // Function to flip a tile when clicked
    function flipTile(tile, val) {
        var $tile = $(tile);
        if ($tile.html() === "" && $('.flipped').length < 2) {
            $tile.css('background', '#f0f4f9');
            // Create an img element and set its src attribute
            var $img = $('<img>').attr('src', val).attr('alt', 'Image');
            // Append the img element to the tile
            $tile.append($img).addClass('flipped');
            if ($('.flipped').length === 2) {
                setTimeout(checkPair, 700);
            }
        }
    }

    // Function to check if two flipped tiles form a pair
    function checkPair() {
        var $flippedTiles = $('.flipped');
        var values = $flippedTiles.map(function() {
            return $(this).find('img').attr('src');
        }).get();
        if (values[0] === values[1]) {
            $flippedTiles.removeClass('flipped').addClass('matched');
            flipped += 2;
            if (flipped === pairs.length) {
                setTimeout(function() {
                    alert("Congratulations! You've finished the game!");
                    $('#game-board').empty();
                    createGameBoard();
                }, 1200);
            }
        } else {
            setTimeout(function() {
                $flippedTiles.css('background', '#d4dfed').html('').removeClass('flipped');
            }, 300);
        }
    }

    // Function to create the game board
    function createGameBoard() {
        flipped = 0;
        var output = ''; // Initialize the output variable to store the HTML content of the game board
        var flipCount = 0;
        $('#flip-count').text("Flips: " + flipCount);

        pairs = shuffleArray(pairs);
        for (var i = 0; i < pairs.length; i++) {
            output += '<div id="tile_' + i + '" class="tile"></div>';
        }
        $('#game-board').html(output);

        // Attach click event handler to dynamically created tiles
        $('#game-board').on('click', '.tile', function() {
            var index = $(this).index();
            flipTile(this, pairs[index]);
        });
    }

    // Initialize the game board
    createGameBoard();
});