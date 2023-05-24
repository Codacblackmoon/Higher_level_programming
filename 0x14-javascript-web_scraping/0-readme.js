#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The first argument is the file path
const file = processa.argv[2];
// The content of the file msut be writen in utf-8
fs.readfile(file, 'utf8', function (err, data) {
	// if an error occed during the reading, print the error object
	if (err) {
		console.log(err);
	} else {
		process.stdout.write(data);
	}
});
