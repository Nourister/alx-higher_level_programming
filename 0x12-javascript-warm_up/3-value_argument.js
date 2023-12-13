#!/usr/bin/node
// Check if the first argument is provided
const firstArgument = process.argv[2];

// Use console.log(...) to print the output
if (firstArgument === undefined) {
  console.log("No argument");
} else {
  console.log(firstArgument);
}
