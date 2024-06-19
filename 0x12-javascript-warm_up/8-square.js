#!/usr/bin/node
const x = process.argv[2];
let i = 0;
if (x !== undefined && parseInt(x, 10)) {
  while (i < parseInt(x, 10)) {
    console.log('X'.repeat(Number(x)));
    i++;
  }
} else {
  console.log('Missing size');
}
