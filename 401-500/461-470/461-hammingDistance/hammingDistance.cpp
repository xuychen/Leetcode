class Solution {
public:
    int hammingDistance(int x, int y) {
        int count = 0;
        for (int setBits = x ^ y; setBits; setBits = setBits & (setBits-1), ++count);
        return count;
    }
};