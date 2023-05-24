#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The first argument is the file path
const file = process.argv[2];
// The second argument is the string to write
const file = process.argv[3];
// The content of the file must be written in utf-8
fs.writefile(file, text, 'utf8', function (err, data) {
	// if an error occed during the reading, print the error object
	if (err) {
		console.log(err);
	}
});
