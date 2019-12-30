'use strict';

 /** 
 * This is an adaptation of partial AstroTime class done by <ict-scheduling [at] alma [dot] cl>
 * https://bitbucket.sco.alma.cl/projects/ASW/repos/icd/browse/SharedCode/gui/src/alma/common/gui/components/astrotime/AstroTime.java 
 * Original work was done by P.Grosbol, ESO, <pgrosbol [at] eso [dot] org>.
 */

 /**
 * Computes J2000
 * @return {number} In milliseconds
 */
var getJ2000 = function() {
    var GregorianCalendar = require('gregorian-calendar');
    var gc2000 = new GregorianCalendar(require('./lib/locale/utc'));
    gc2000.set(2000,0,1,12,0,0);
    return gc2000.getTime();
}

 /**
 * Computes the Mean Siderical Time at Greenwich
 * @param {date} date time for which GMST should be computed
 * @return {number} Greenwich Mean Siderical Time in hours
 */
var getGMST = function(date) {
    var j2000 = getJ2000();
    var msday = 86400000.0;
    var jcent = 36525.0;

    var du  = (date.getTime() - j2000) / msday;
    var df = du - Math.floor(du);
    var th = 0.7790572732640 + 0.00273781191135448*du + df;

    th -= Math.floor(th);
    var tc = du/jcent;

    var gmst = 24.0*th+(0.014506 +
        tc*(4612.156534 +
        tc*(1.3915817 -
            tc*(0.00000044 +
            tc*(0.000029956 +
                tc*0.0000000368)))))/(54000.0);

    gmst -= Math.floor(gmst/24.0)*24.0;
    return gmst;
}

 /** 
 * Gets Local Siderical Time for site at given date
 * @param  date time for which to calculate LST
 * @param  lon  longitude of site in degress (East positive)
 * @return LST in hours for longitude specified
 */
var getLST = function(date, lon) {
    var gmst = getGMST(date);
    var lst = gmst + lon/15.0 + 240.0;
    return lst - Math.floor(lst/24.0)*24.0;
}

var toString = function(lst) {
    var hour = parseInt(lst);
    var minutes = parseInt((lst - parseInt(lst)) * 60);

    var haStr = "";

    haStr += hour < 10 ? '0' : '';
    haStr += hour

    haStr += ':'

    haStr += minutes < 10 ? '0' : '';
    haStr += minutes;
    
    return haStr;
}

 /** 
 * Gets Local Siderical Time for site at given date
 * @param {date} date time for which to claculate LST
 * @param {number} lon  longitude of site in degress (East positive)
 * @return LST in hours:minutes string representation
 */
var lstString = function(date, lon) {
    var gmst = getGMST(date);
    var lst = gmst + lon/15.0 + 240.0;
    lst = getLST(date, lon);
    return toString(lst);
}

exports.getJ2000 = getJ2000;
exports.getGMST = getGMST;
exports.getLST = getLST;
exports.toString = toString;
exports.lstString = lstString;
