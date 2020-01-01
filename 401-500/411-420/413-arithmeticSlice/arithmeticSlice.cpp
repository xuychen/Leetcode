#include <vector>

using namespace std;

class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& a) {
        int result = 0;
        if (a.size() < 3)
            return result;

        int prev = a[1] - a[0], count = 1;

        for (size_t i = 2; i < a.size(); ++i) {
            int difference = a[i] - a[i-1];
            count = difference == prev ? count + 1 : 1;
            if (count >= 2)
                result += count - 1;

            prev = difference;
        }

        return result;
    }
};