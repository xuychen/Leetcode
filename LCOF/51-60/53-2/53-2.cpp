class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int left, right;
        left = 0, right = nums.size();
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= mid)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }
};