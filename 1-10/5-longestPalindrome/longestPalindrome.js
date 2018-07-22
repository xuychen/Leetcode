/**
 * @param {string} s
 * @return {string}
 */

var longestPalindrome = function(s) {
    let newString =  "$#" + s.split("").join("#") + "#";
    let lps = [0];
    let center = 0, maxRight = 0, resultCenter = 0, resultLength = 0;
    
    for (let index = 1; index <= s.length * 2; index++) {
        let next = index < maxRight ? Math.min(lps[2*center-index], maxRight-index) : 1;
        lps.push(next);
        while (newString[index + lps[index]] == newString[index - lps[index]]) ++lps[index];
        
        if (maxRight < index + lps[index]) {
            maxRight = index + lps[index];
            center = index;
        }
        
        if (resultLength < lps[index]) {
            resultLength = lps[index];
            resultCenter = index;
        }
    }
    
    return s.substr((resultCenter - resultLength) / 2, resultLength - 1);
};