$(document).ready(function() {
    $('#table1').find('th').click(function() {
        var table = $(this).closest('table');
        var n = $(this).index();
        var switching = true;
        var dir = "asc";
        var switchcount = 0;

        while (switching) {
            switching = false;
            x = table.rows[n].cells; // Get the cells of the specified column

            for (var i = 1; i < (x.length - 1); i++) {
                var shouldSwitch = false;

                var a = $(x[i]).text().toLowerCase();
                var b = $(x[i + 1]).text().toLowerCase();

                var numA = parseFloat(a);
                var numB = parseFloat(b);

                if (!isNaN(numA) && !isNaN(numB)) {
                    a = numA;
                    b = numB;
                }

                if (dir == "asc") {
                    if (a > b) {
                        shouldSwitch = true;
                        break;
                    }
                } else if (dir == "desc") {
                    if (a < b) {
                        shouldSwitch = true;
                        break;
                    }
                }
            }

            if (shouldSwitch) {
                // Exchange columns
                for (var j = 0; j < table.rows.length; j++) {
                    var copie = table.rows[j].cells[i].innerHTML;
                    table.rows[j].cells[i].innerHTML = table.rows[j].cells[i + 1].innerHTML;
                    table.rows[j].cells[i + 1].innerHTML = copie;
                }

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