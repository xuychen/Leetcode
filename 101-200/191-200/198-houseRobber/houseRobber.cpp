class Solution {
public:
    int rob(vector<int>& nums) {
        int length = nums.size();
        vector<int> dp = vector<int> (length);

        if (length == 0)
            return 0;
        if (length == 1)
            return nums[0];
        
        dp[0] = nums[0];
        dp[1] = max(nums[1], dp[0]);

        for (int i = 2; i < nums.size(); ++i)
            dp[i] = max(dp[i-2] + nums[i], dp[i-1]);

        return dp[nums.size()-1];
    }
};