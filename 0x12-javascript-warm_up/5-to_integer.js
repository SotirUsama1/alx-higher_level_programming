#!/usr/bin/node
if (parseInt(process.argv[2], 10)) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
