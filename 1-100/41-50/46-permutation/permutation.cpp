#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        helper(nums, ans, 0);
        return ans;
    }
    
    void helper(vector<int> &nums, vector<vector<int>> &ans, int index) {
        if (index == nums.size())
            ans.push_back(nums);
        
        for (int i = index; i < nums.size(); ++i) {
            swap(nums[i], nums[index]);
            helper(nums, ans, index+1);
            swap(nums[i], nums[index]);
        }       
    }
};