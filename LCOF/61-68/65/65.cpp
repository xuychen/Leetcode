class Solution {
public:
    int add(int a, int b) {
        bool carryOn = false;
        int result = 0;

        for (unsigned int bit = 1; bit != 0; bit <<= 1) {
            int carryOn_bit = carryOn ? bit : 0;
            result |= ((a & bit) ^ (b & bit) ^ carryOn_bit);
            carryOn = ((a & bit) && (b & bit)) || ((a & bit) && carryOn) || ((b & bit) && carryOn);
        }

        return result;
    }
};