// Script that toggles the class of the header element when the user clicks on the tag id.
const headerelement = document.querySelector('toggle_header');
headerelement.addEventListener('click', function() {
    var headelement = document.querySelector('h1');
    if (headelement.classList.contains('red')) {
        headelement.classList.remove('red');
        headelement.classList.add('green');
    } else if (headelement.classList.contains('green')) {
        headelement.classList.remove('green');
        headelement.classList.add('red');
    }
});
