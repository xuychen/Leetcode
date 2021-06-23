#include <unordered_set>

using namespace std;

class Solution {
public:
    bool isStraight(vector<int>& nums) {
        int low = 14, high = -1;
        unordered_set<int> numbers;

        for (int it: nums) {
            if (it == 0)
                continue;

            low = min(it, low);
            high = max(it, high);
            if (high - low >= 5 || numbers.find(it) != numbers.end())
                return false;

            numbers.insert(it);
        }

        return true;
    }
};