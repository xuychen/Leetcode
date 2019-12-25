#include <vector>

using namespace std;

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int storeIndex = 0;

        for (auto &it: nums)
            if (storeIndex == 0 || it != nums[storeIndex-1])
                nums[storeIndex++] = it;

        return storeIndex;
    }
};