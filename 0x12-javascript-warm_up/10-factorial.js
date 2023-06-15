#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) {
    return 1;
  }
  if (num === 0) {
    return 1;
  } else {
    return num * factorial(num - 1);
  }
}
const input = parseInt(process.argv[2]);
const result = factorial(input);
console.log(`Factorial of ${input} is: ${result}`);
