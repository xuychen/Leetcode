#include <vector>

using namespace std;

class Solution {
public:
    int nthUglyNumber(int n) {
        vector<int> uglyNumbers = {1};

        for (int i = 1, i2 = 0, i3 = 0, i5 = 0; i < n; ++i) {
            int next_number = min(uglyNumbers[i2] * 2, min(uglyNumbers[i3] * 3, uglyNumbers[i5] * 5));
            if (next_number == uglyNumbers[i2] * 2)
                ++i2;
            if (next_number == uglyNumbers[i3] * 3)
                ++i3;
            if (next_number == uglyNumbers[i5] * 5)
                ++i5;

            uglyNumbers.push_back(next_number);
        }

        return uglyNumbers.back();
    }
};