#!/usr/bin/node
/*
this package prints args parsed to the file else
it prints No argument
*/

const args = process.argv;
if (args.length === 2) {
    console.log("No argument");
}
else {
    console.log(args[2]);
}
