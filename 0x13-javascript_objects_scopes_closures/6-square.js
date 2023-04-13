#!/usr/bin/nodee
module.exports = class spuate extends require('.5-rectangle.js') {
	charPrint (c) {
		if (c === undefined) {
			this.print();
		} else {
			for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
		}
	}
};
