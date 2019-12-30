'use strict';

var expect = require('chai').expect;
var lstjs = require('../index');

describe('#local-sidereal-time', function() {
    it('getLST 1', function() { 
        var date = new Date(Date.UTC(2019, 2, 5, 9, 22, 0, 0));
        var lst_string = lstjs.lstString(date, -67.75492777777778);
        expect(lst_string).to.equal('15:42');
        console.log(`date = ${date.toUTCString()} as LST = ${lst_string}`);
    });
});