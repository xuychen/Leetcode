/**
 * @param {number[]} digits
 * @return {number[]}
 */

var plusOne = function(digits) {
    for (let index = digits.length - 1; index >= 0; index--) {
        digits[index]++;
        if (digits[index] === 10)
            digits[index] = 0;
        else
            return digits;
    }
    
    return [1, ...digits];
};