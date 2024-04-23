document.addEventListener("DOMContentLoaded", function() {
    // Attach an event listener to the 'change' event of the 'date' input field
    document.forms["form-container"]["date"].addEventListener("change", calculateAge);
});

// Function to calculate age based on the provided date of birth
function calculateAge() {
    let dateOfBirth = new Date(document.forms["form-container"]["date"].value);
    let currentDate = new Date();
    let age = currentDate.getFullYear() - dateOfBirth.getFullYear();

    document.forms["form-container"]["age"].value = age;
}

// Function to validate the form
function validateForm() {
    let name = document.forms["form-container"]["name"].value;
    let date = document.forms["form-container"]["date"].value;
    let email = document.forms["form-container"]["email"].value;

    var error = "";

    // Validate the 'name' field
    if (checkEmpty(name)) {
        error += "Campul nume nu este completat\n";
        document.forms["form-container"]["name"].style.border = "1px solid red";
    } else if (!checkOnlyLetters(name)) {
        error += "Campul nume nu este valid. Completati doar cu litere.\n";
        document.forms["form-container"]["name"].style.border = "1px solid red";
    } else {
        document.forms["form-container"]["name"].style.border = "none";
    }

    // Validate the 'date' field
    if (checkEmpty(date)) {
        error += "Campul data nu este completat\n";
        document.forms["form-container"]["date"].style.border = "1px solid red";
    } else {
        document.forms["form-container"]["date"].style.border = "none";
    }

    // Validate the 'email' field
    if (checkEmpty(email)) {
        error += "Campul email nu este completat\n";
        document.forms["form-container"]["email"].style.border = "1px solid red";
    } else if (!checkEmail(email)) {
        error += "Campul email nu este valid. Respectati formatul username@domain.xx.\n";
        document.forms["form-container"]["email"].style.border = "1px solid red";
    } else {
        document.forms["form-container"]["email"].style.border = "none";
    }

    if (error.length > 0) {
        alert(error);
        return false;
    } else {
        alert('Datele sunt completate corect');
        return false;
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
    return field === "";
}