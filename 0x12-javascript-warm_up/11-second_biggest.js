#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(Number);

if (numbers.length <= 1) {
  console.log(0);
} else {
  const maxNumber = Math.max(...numbers);
  const secondMax = Math.max(...numbers.filter((num) => num !== maxNumber));
  console.log(secondMax);
}
