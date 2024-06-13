$(document).ready(function() {
	// Attach an event listener to the 'change' event of the 'date' input field
	$('#date').on('change', calculateAge);

	// Attach an event listener to the form submission
	$('#myForm').on('submit', function(event) {
		event.preventDefault(); // Prevent default form submission

		// Validate the form
		if(validateForm()) {
			alert('Datele sunt completate corect');
		}
	});

});

// Function to calculate age based on the provided date of birth
function calculateAge() {
	var date = new Date($('#date').val());
	var currentDate = new Date();
	var age = currentDate.getFullYear() - date.getFullYear();

	$('#age').val(age);
}

// Function to validate the form
function validateForm() {
	var name = $('#name').val().trim();
	var date = $('#date').val().trim();
	var email = $('#email').val().trim();
	var error = "";

	// Validate the 'name' field
	if (checkEmpty(name)) {
		error += "Campul nume nu este completat\n";
		$('#name').addClass('error');
	}
	else if(!checkOnlyLetters(name)) {
		error += "Campul nume nu este valid. Completati doar cu litere.\n";
		$('#name').addClass('error');
	}
	else {
		$('#name').removeClass('error');
	}

	// Validate the 'date' field
	if (checkEmpty(date)) {
		error += "Campul data nu este completat\n";
		$('#date').addClass('error');
	}
	else {
		$('#date').removeClass('error');
	}

	// Validate the 'email' field
	if (checkEmpty(email)) {
		error += "Campul email nu este completat\n";
		$('#email').addClass('error');
	}
	else if(!checkEmail(email)) {
		error += "Campul email nu este valid. Respectati formatul username@domain.xx.\n";
		$('#email').addClass('error');
	}
	else {
		$('#email').removeClass('error');
	}

	if (error.length > 0) {
		alert(error);
		return false;
	} else {
		return true;
	}
}

// Function to check if a word contains only letters
function checkOnlyLetters(word) {
	return /^[a-zA-Z]+$/.test(word);
}

// Function to check if an email is valid
function checkEmail(email) {
	return /\S+@\S+\.\S+/.test(email);
}

// Function to check if a field is empty
function checkEmpty(field) {
	return field == "";
}