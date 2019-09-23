#!/usr/bin/node
exports.esrever = function (list) {
  let repList = [];
  for (let i = 0; i < list.length; i++) {
    repList.unshift(list[i]);
  }
  return repList;
};
