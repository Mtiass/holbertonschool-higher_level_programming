// Script that fetches and lists the title for all movies by using this URL.
function fetchMovieTitlesAndUpdate() {
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
      .then(response => response.json())
      .then(data => {
            var movieTitles = data.results.map(movie => movie.title);
            var movieList = document.getElementById('list_movies');
            movieList.innerHTML = '';
            movieTitles.forEach(title => {
                var listItem = document.createElement('li');
                listItem.textContent = title;
                movieList.appendChild(listItem);
            });
        })
      .catch(error => console.error('Error fetching movie data:', error));
}
