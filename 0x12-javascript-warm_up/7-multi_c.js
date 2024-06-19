#!/usr/bin/node
const x = process.argv[2];
if (x === undefined) {
  console.log('Missing number of occurrences');
} else if (x > 0) {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}
