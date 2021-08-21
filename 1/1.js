/**
 * @param {string} s
 * @return {boolean}
 */

 function isAlphaNumeric(str) {
  var code, i, len;

  for (i = 0, len = str.length; i < len; i++) {
    code = str.charCodeAt(i);
    if (!(code > 47 && code < 58) && // numeric (0-9)
        !(code > 64 && code < 91) && // upper alpha (A-Z)
        !(code > 96 && code < 123)) { // lower alpha (a-z)
      return false;
    }
  }
  return true;
    
    // return str.match(/^[a-z0-9]+$/i);
};

var isPalindrome = function(s) {
    let strs = [];
    for (char of s) {
        // if (char.match(/^[a-z0-9]+$/i)) {
        if (isAlphaNumeric(char)) {
          strs.push(char.toLowerCase());
        }
    }

    while (strs.length > 1) {
        if (strs.shift() !== strs.pop()) {
          return false;
        }
    }

    return true;
};
