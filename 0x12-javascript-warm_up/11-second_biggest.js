#!/usr/bin/node
let argList = process.argv;
if (argList.length <= 3) {
  console.log(0);
} else {
  console.log(argList.sort().reverse()[1]);
}
