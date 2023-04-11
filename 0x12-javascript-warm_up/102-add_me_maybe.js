#!/usr/bin/node
exports.addMEMaybe = function (number, theFunction) {
	theFunction(++number);
};
