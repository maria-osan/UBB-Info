function sortTable(n, x, tableType) {
   	if(tableType == 'vertical') {
   		var rows, i, j, x, shouldSwitch, switchcount = 0,
           copie;
        var idTable = x.parentNode.parentNode.parentNode.id; // Get the ID of the table
        var table = document.getElementById(idTable); // Get the table element by ID
        var switching = true;

        var dir = "asc";
        while (switching) {
            switching = false;
            x = table.rows[n].cells; // Get the cells of the specified column
            // Loop through the cells
            for (i = 1; i < (x.length - 1); i++) {
                shouldSwitch = false;

                var a = x[i].innerHTML.toLowerCase();
	            var b = x[i + 1].innerHTML.toLowerCase();

	            // Convert x and y to numbers if possible
				var numA = parseFloat(a);
				var numB = parseFloat(b);

				if (!isNaN(numA) && !isNaN(numB)) {
				    // If both are numbers, compare them numerically
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
                // exchange columns
                for (j = 0; j < table.rows.length; j++) {
                    copie = table.rows[j].cells[i].innerHTML
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
   	} else if(tableType == 'horizontal') {
   		var rows, i, j, x, shouldSwitch, switchcount = 0,
           copie;
        var idTable = x.parentNode.parentNode.parentNode.id; // Get the ID of the table
        var table = document.getElementById(idTable); // Get the table element by ID
        var switching = true;

        var dir = "asc";
        while (switching) {
			switching = false;
	        rows = table.rows; // Get all the rows of the table
	        // Loop through the rows
	        for (i = 1; i < (rows.length - 1); i++) {
	            shouldSwitch = false;

	            var x = rows[i].getElementsByTagName("td")[n].innerHTML.toLowerCase();
	            var y = rows[i + 1].getElementsByTagName("td")[n].innerHTML.toLowerCase();

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
	        	// Swap the position of rows
	            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
	            switching = true;
	            switchcount++;
	        } else {
	            if (switchcount == 0 && dir == "asc") {
	                dir = "desc";
	                switching = true;
	            }
	        }
        }
   	}
}