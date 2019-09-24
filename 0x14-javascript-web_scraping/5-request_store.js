#!/usr/bin/node
const fs = require('fs');
const request = require('request');
let url = process.argv[2];
let file = process.argv[3];
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  fs.writeFile(file, body, (err) => {
    if (err) console.log(err);
  });
});
