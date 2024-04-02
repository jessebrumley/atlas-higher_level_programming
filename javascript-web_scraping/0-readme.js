#!/usr/bin/node
/* A script that reads and prints the content of a file. */

const fs = require('fs');

if (process.argv[2] === undefined) {
  console.log('No filename provided');
} else {
  fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
      console.error(err);
    } else {
      console.log(data);
    }    
  });
}
