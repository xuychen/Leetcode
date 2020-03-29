#include <vector>
#include <set>

using namespace std;

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        set<vector<int>> ans;
        helper(nums, ans, 0);
        return {ans.begin(), ans.end()};
    }
    
    void helper(vector<int> &nums, set<vector<int>> &ans, int index) {
        if (index == nums.size())
            ans.insert(nums);
        
        for (int i = index; i < nums.size(); ++i) {
            swap(nums[i], nums[index]);
            helper(nums, ans, index+1);
            swap(nums[i], nums[index]);
        }       
    }
};