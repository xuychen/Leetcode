#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> addToArrayForm(vector<int>& a, int k) {
        vector<int> result;

        for (int i = a.size() - 1, carryOn = 0; i >= 0 || k || carryOn; --i, k /= 10) {
            int value = (i >= 0 ? a[i] : 0) + k % 10 + carryOn;
            carryOn = value / 10;
            value -= carryOn * 10;

            result.push_back(value);
        }

        reverse(result.begin(), result.end());
        return result;
    }
};