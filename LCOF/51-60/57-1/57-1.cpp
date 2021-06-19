class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;

        while (left < right)
            if (nums[left] + nums[right] == target)
                return {nums[left], nums[right]};
            else if (nums[left] + nums[right] < target)
                left += 1;
            else
                right -= 1;

        return vector<int>();
    }
};