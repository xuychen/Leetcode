#include <vector>

#define DIVISOR 60

using namespace std;

class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        vector<int> numMap = vector<int> (60, 0);
        int result = 0;

        for (auto it: time) {
            result += numMap[(600 - it) % DIVISOR];
            ++numMap[it % DIVISOR];
        }

        return result;
    }
};