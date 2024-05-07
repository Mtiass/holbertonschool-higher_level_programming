// Script that adds a li element to a list when the user clicks on the element with id add_item.
const additem = document.querySelector('#add_item');
additem.addEventListener('click', function() {
    var newitem = document.createElement('li');
    newitem.textContent = "Item";
    var myList = document.querySelector('.my_list');
    myList.appendChild(newitem);
});
