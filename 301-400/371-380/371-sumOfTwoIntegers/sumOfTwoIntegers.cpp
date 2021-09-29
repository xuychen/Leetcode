class Solution {
public:
    int getSum(int a, int b) {
        unsigned int carry_on;

        while (b) {
            carry_on = a & b;
            a ^= b;
            b = carry_on << 1;
        }

        return a;
    }
};