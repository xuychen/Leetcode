#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        auto riter =  nums.rbegin() + 1, riter2 = nums.rbegin();
        for (; riter != nums.rend(); ++riter)
            if (*riter < *(riter-1))  {
                for (; *riter >= *riter2; ++riter2);
                swap(*riter, *riter2);
                break;
            }
        
        reverse(nums.rbegin(), riter);
    }
};