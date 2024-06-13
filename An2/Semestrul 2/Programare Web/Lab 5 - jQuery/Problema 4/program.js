$(document).ready(function() {
    $('#table3').find('th').click(function() {
        var table = $(this).closest('table');
        var columnIndex = $(this).index();
        var switching = true;
        var dir = "asc";
        var switchcount = 0;

        while (switching) {
            switching = false;
            var rows = table.find('tr').toArray();
            
            for (var i = 1; i < (rows.length - 1); i++) {
                var shouldSwitch = false;
                var x = $(rows[i]).find('td').eq(columnIndex).text().toLowerCase();
                var y = $(rows[i + 1]).find('td').eq(columnIndex).text().toLowerCase();

                // Convert x and y to numbers if possible
                var numX = parseFloat(x);
                var numY = parseFloat(y);

                if (!isNaN(numX) && !isNaN(numY)) {
                    // If both are numbers, compare them numerically
                    x = numX;
                    y = numY;
                }

                if (dir == "asc") {
                    if (x > y) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (x < y) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }

            if (shouldSwitch) {
                $(rows[i]).insertAfter(rows[i + 1]);
                switching = true;
                switchcount++;
            } else {
                if (switchcount == 0 && dir == "asc") {
                    dir = "desc";
                    switching = true;
                }
            }
        }
    });
});