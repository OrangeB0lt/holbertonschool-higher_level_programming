/ fetches and prints san francisco wind speed
let url = 'https://fourtonfish.com/hellosalut/?lang=' + lang;
$.get(url, function (data, status) {
  if (status === 'success') {
    $('DIV#hello').text(data.hello);
  }
});
