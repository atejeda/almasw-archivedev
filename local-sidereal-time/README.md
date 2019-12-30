[![Build Status](https://travis-ci.org/atejeda/local-sidereal-time.svg?branch=master)](https://travis-ci.org/atejeda/local-sidereal-time)

[![Coverage Status](https://coveralls.io/repos/github/atejeda/local-sidereal-time/badge.svg)](https://coveralls.io/github/atejeda/local-sidereal-time)

# Local Sidereal Time (nmp module)

A small library to get the local sidereal time based at a given longitud and date.

It has a helper for getting the LST in hours and as a string up to in minutes resolution for GUI purposes.

This is an adaptation of partial AstroTime class done by <ict-scheduling [at] alma [dot] cl>

[Original work](https://bitbucket.sco.alma.cl/projects/ASW/repos/icd/browse/SharedCode/gui/src/alma/common/gui/components/astrotime/AstroTime.java ) was done by P.Grosbol, ESO, <pgrosbol [at] eso [dot] org>.

## Installation

    npm i -S local-sidereal-time

## Usage

Given date should be UTC.

    var lstjs = require('local-sidereal-time');
    var date = new Date(Date.UTC(2019, 2, 5, 9, 22, 0, 0));
    var lst_hours = lstjs.getLST(date, -67.75492777777778)
    var lst_string = lstjs.lstString(date, -67.75492777777778);
    # lst_string should be '15:42';

## Tests

  `npm test`

## Contributing

In lieu of a formal style guide, take care to maintain the existing coding style. Add unit tests for any new or changed functionality. Lint and test your code, pull request as needed.

## License

Original work is being licensed under GPL-2.0, this follows the same license, refer to [GNU](https://www.gnu.org/licenses/gpl-2.0.txt) site for details.
