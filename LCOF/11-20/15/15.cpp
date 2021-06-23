class Solution {
public:
    int hammingWeight(uint32_t n) {
        int count = 0;
        for (unsigned int m = n; m != 0; m >>= 1)
            count += m & 1;

        return count;
    }
};