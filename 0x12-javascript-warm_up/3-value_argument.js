#!/usr/bin/node
function argument(a) {
	if (a === 1) {
		console.log('Argument found');
	} else if (a === 0)  {
		console.log('No argument found');
	} else {
		console.log('Arguments found');
	}
}
const a = 1; // Assign the value of a here
argument(a);
