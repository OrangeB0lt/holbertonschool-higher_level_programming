#!/usr/bin/node
const request = require('request');
let url = 'http://swapi.co/api/films/';
let epiNum = process.argv[2];
request(url + epiNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Wrong status code');
  }
});
