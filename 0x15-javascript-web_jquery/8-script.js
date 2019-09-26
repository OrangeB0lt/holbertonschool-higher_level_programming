// fetches and lists all movie titles using url
$.get('https://swapi.co/api/films/?format=json', function (data, status) {
  if (status === 'success') {
    for (let count in data.results) {
      $('UL#list_movies').append('<li>' + data.results[count].title + '</li>');
    }
  }
});
