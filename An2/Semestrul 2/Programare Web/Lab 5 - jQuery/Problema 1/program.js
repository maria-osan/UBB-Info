$(document).ready(function() {
	// Function to move items from one list to another
	function moveItems(source, destination) {
		$(source).find(':selected').appendTo(destination);
	}

	// Double click event handler for list1
	$('#list1').on('dblclick', 'option', function() {
		moveItems('#list1', '#list2');
	});

	// Double click event handler for list2
	$('#list2').on('dblclick', 'option', function() {
		moveItems('#list2', '#list1');
	});
});