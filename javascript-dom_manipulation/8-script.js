// Script that fetches from URL and displays the value of hello.
function fetchTranslationAndUpdate() {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
        var helloTranslation = data.hello;
        document.getElementById('hello').textContent = helloTranslation;
    })
    .catch(error => console.error('Error fetching translation:', error));
}
