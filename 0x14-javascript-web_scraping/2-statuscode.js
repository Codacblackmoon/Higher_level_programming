#!/usr/bin/node
const process = require('process');
const request = require('request');

// The first argument is the file path
const file = process.argv[2];

request(url, function (error, response) {
	if (error == null) {
		// display the status code of a GET request.
		console.log(`code: ${response.statusCode}`);
	}
});
