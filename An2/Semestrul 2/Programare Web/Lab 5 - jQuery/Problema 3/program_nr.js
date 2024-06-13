$(document).ready(function() {
    var numbers = []; // Stores the numbers currently flipped
    var tile_ids = []; // Stores the IDs of the tiles flipped
    var flipped = 0; // Counts the number of flipped pairs
    var pairs = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8];

    // Shuffle function to randomly shuffle the pairs array
    Array.prototype.shuffle = function() {
        var i = this.length,
            j, aux;
        while (--i > 0) {
            j = Math.floor(Math.random() * (i + 1));
            aux = this[i];
            this[i] = this[j];
            this[j] = aux;
        }
    };

    // Function to flip a tile when clicked
    function flipTile(tile, val) {
        var $tile = $(tile);
        if ($tile.text() == "" && $('.flipped').length < 2) {
            $tile.css('background', '#f0f4f9').text(val).addClass('flipped');
            if ($('.flipped').length == 2) {
                setTimeout(checkPair, 700);
            }
        }
    }

    // Function to check if two flipped tiles form a pair
    function checkPair() {
        var $flippedTiles = $('.flipped');
        var values = $flippedTiles.map(function() {
            return $(this).text();
        }).get();
        if (values[0] === values[1]) {
            $flippedTiles.removeClass('flipped').addClass('matched');
            flipped += 2;
            if (flipped == pairs.length) {
                setTimeout(function() {
                    alert("Congratulations! You've finished the game!");
                    $('#game-board').empty();
                    createGameBoard();
                }, 1200);
            }
        } else {
            setTimeout(function() {
                $flippedTiles.css('background', '#d4dfed').text('').removeClass('flipped');
            }, 300);
        }
    }

    // Function to create the game board
    function createGameBoard() {
        flipped = 0;
        var output = ''; // Initialize the output variable to store the HTML content of the game board

        pairs.shuffle();
        for (var i = 0; i < pairs.length; i++) {
            output += '<div class="tile" id="tile_' + i + '"></div>';
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