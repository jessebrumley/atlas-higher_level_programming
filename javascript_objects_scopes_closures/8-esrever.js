#!/usr/bin/node
/*
A function that returns the reversed version of a list
*/
exports.esrever = function (list) {
  let reverseList = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverseList.push(list[i]);
  }
  return (reverseList);
};
