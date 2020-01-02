/*
IDEA SOURCE
For convenience, say n is sufficiently large and can be broken into any smaller real positive numbers. We now try to calculate which real number generates the largest product.
Assume we break n into (n / x) x's, then the product will be x^(n/x), and we want to maximize it.

Taking its derivative gives us n * x^(n/x-2) * (1 - ln(x)).
The derivative is positive when 0 < x < e, and equal to 0 when x = e, then becomes negative when x > e,
which indicates that the product increases as x increases, then reaches its maximum when x = e, then starts dropping.

This reveals the fact that if n is sufficiently large and we are allowed to break n into real numbers,
the best idea is to break it into nearly all e's.
On the other hand, if n is sufficiently large and we can only break n into integers, we should choose integers that are closer to e.
The only potential candidates are 2 and 3 since 2 < e < 3, but we will generally prefer 3 to 2. Why?

Of course, one can prove it based on the formula above, but there is a more natural way shown as follows.

6 = 2 + 2 + 2 = 3 + 3. But 2 * 2 * 2 < 3 * 3.
Therefore, if there are three 2's in the decomposition, we can replace them by two 3's to gain a larger product.
*/

#include <cmath>

class Solution {
public:
    int integerBreak(int n) {
        if (n < 4)
            return n - 1;

        int totalTimes = n / 3;

        switch (n - 3 * totalTimes) {
            case 0:
                return pow(3, totalTimes);
            case 1:
                return 4 * pow(3, totalTimes - 1);
            case 2:
                return 2 * pow(3, totalTimes);
            default:
                return -1;
        }
    }
};