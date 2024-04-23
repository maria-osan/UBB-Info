// Function to move selected option from one select element to another
function moveOption(fromId, toId)
{
    var fromSelect = document.getElementById(fromId); // source select element
    var toSelect = document.getElementById(toId); // destination select element
    
    var selectedOption = fromSelect.options[fromSelect.selectedIndex]; // the selected option from the source select element
    
    if (selectedOption)
    {
        toSelect.appendChild(selectedOption);
    }
}