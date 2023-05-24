#!/usr/bin/node
const request = require('request');

// first argument is the API URL
const URL = process.argv{2};

request(URL, (error, response, body) => {
	if (error) {
		console.log(error);
	} else if (body) {
		// Wedge Antilles is character Id 18 - use this Id for filtering the
		// result of the API
		const json = JSON.results.filer;
		const charFilms = json.results.filter(
			x => x.characters.find(y => y.match(/\/people\/?$/))
		);
		console.log(charFilms.length);
	}
});
