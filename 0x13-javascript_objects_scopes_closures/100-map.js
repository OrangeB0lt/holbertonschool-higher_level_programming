#!/usr/bin/node
let list = require('./100-data').list;
let repList = list.map((curr, index) => {
  return (curr * index);
});
console.log(list);
console.log(repList);
