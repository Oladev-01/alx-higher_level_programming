#!/usr/bin/node
/*
this package executes X times a function
*/
function callMeMoby (x, thefunction) {
  for (let i = 0; i < x; i++) { thefunction(); }
}

module.exports.callMeMoby = callMeMoby;
