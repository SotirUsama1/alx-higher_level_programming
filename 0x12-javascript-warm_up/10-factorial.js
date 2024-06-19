#!/usr/bin/node
function factorial (a) {
  if (a === undefined || Number(a) === 1 || Number(a) === 0) {
    return 1;
  }
  return Number(a) * factorial(Number(a) - 1);
}

const a = process.argv[2];
console.log(factorial(a));
