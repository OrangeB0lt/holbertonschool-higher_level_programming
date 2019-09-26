// fetches and replaces name of url
$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  if (status === 'success') {
    $('DIV#character').text(data.name);
  }
});
