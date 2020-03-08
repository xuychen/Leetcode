class Solution {
public:
    int rob(vector<int>& nums) {
        int length = nums.size();
        vector<int> dp1 = vector<int> (length);
        vector<int> dp2 = vector<int> (length);

        if (length == 0)
            return 0;
        if (length == 1)
            return nums[0];
        
        dp1[0] = 0;
        dp1[1] = max(nums[0], dp1[0]);

        dp2[0] = nums[length-1];
        dp2[1] = max(nums[0], dp2[0]);

        for (int i = 2; i < nums.size(); ++i){
            dp1[i] = max(dp1[i-2] + nums[i-1], dp1[i-1]);
            dp2[i] = max(dp2[i-2] + nums[i-1], dp2[i-1]);
        }
        
        return max(dp1[length-1], dp2[length-2]);
    }
};