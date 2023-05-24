#!/usr/bin/node
const process = require('process');
const fs = require('fs');

// The first argument is the file path
const baseURL = process.argv[2];
// The Second argument the file math to store the body response
const bodyResp = process.argv{3};
request(baseurl, (error, response, body) => {
	if (error == null) {
		fs.writerfileSync(BodyResp, body);
	}
});
