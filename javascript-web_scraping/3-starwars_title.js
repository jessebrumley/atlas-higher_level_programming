#!/usr/bin/node
/* A script prints the title of a Star Wars movie where the episode number matches a given integer. */
const request = require('request');
const episode = process.argv[2];
const API = 'https://swapi-api.hbtn.io/api/films/';

request(API + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const data = JSON.parse(body);
    console.log(data.title);
  } else {
    console.log('Error code: ' + response.statusCode);
  }
});
