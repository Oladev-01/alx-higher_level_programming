#!/usr/bin/node
/*
this package prints args parsed to the file else
it prints No argument
*/

if (process.argv[2] === undefined) {
    console.log("No argument");
}
else {
    console.log(process.argv[2]);
}
