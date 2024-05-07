// Script that updates text color of the header elnt to red when the us click swith id red_header
const headerelent = document.querySelector('red_header');
headerelent.addEventListener('click', function() {
    var headerElement = document.querySelector('h1');
    headerElement.style.color = "#FF0000";
});
