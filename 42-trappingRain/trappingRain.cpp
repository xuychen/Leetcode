#include <vector>

// a smart answer I got in Leet Code discussion, fast and no additional space

class Solution {
   public:
    int trap(vector<int>& height) {
        auto l = height.begin(), r = height.end() - 1;
        int level = 0, water = 0;
        while (l != r + 1) {
            int lower = *l < *r ? *l++ : *r--;
            level = max(level, lower);
            water += level - lower;
        }
        return water;
    }
};