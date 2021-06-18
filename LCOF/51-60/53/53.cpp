class Solution {
public:
    int bisect_left(vector<int>& nums, int target) {
        int left, right;
        left = 0, right = nums.size();

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] >= target)
                right = mid;
            else
                left = mid + 1;
        }

        return left;
    }

    int bisect_right(vector<int>& nums, int target) {
        int left, right;
        left = 0, right = nums.size();

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (nums[mid] <= target)
                left = mid + 1;
            else
                right = mid;
        }

        return left;
    }

    int search(vector<int>& nums, int target) {
        int left = bisect_left(nums, target);
        int right = bisect_right(nums, target);
        return right - left;
    }
};