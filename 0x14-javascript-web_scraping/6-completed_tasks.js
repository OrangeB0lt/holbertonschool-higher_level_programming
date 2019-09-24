#!/usr/bin/node
const request = require('request');
let url = process.argv[2];
let obj = {};
request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  let jRes = JSON.parse(body);
  for (let i in jRes) {
    if (jRes[i].completed) {
      if (jRes[i].userId in obj) { obj[jRes[i].userId]++; } else { obj[jRes[i].userId] = 1; }
    }
  }
  console.log(obj);
});
