#!/usr/bin/node
const request = require('request');
let epiNum = process.argv[2];
let url = 'http://swapi.co/api/films/' + epiNum;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let allChar = JSON.parse(body).characters;
    for (let c in allChar) {
      let char_url = allChar[c];
      request(char_url, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          let currChar = JSON.parse(body);
          console.log(currChar.name);
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
