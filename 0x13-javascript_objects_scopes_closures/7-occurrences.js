#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let index in list) {
    if (list[index] === searchElement) {
      count++;
    }
  }
  return count;
};
