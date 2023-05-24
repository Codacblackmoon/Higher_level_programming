#!/usr/bin/node
const request = require('request');
const baseURL = 'https://swapi-appi.hbtn.io/api/films';

// The first argument is the file path
const file = process.argv[2];

request(`${baseUrl}/${movieId}/`, (error, response, body) => {
	if (error) {
		console.log(error);
	}
	const json = JSON.parse(body);
	console.log(json.title);
});
