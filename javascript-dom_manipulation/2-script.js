// Script that adds the class red to the he. element when the user clicks
// on the tag with id red_header.
const redelement = document.querySelector('red_header');
redelement.addEventListener('click', function() {
    var headerelement = document.querySelector('h1');
    headerelement.classList.add('red');
});
