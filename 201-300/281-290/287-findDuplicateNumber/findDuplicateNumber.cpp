class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        if (nums.size() > 1) {
            int slow = nums[0];
            int fast = nums[nums[0]];
            while (slow != fast) {
                slow = nums[slow];
                fast = nums[nums[fast]];
            }

            fast = 0;
            while (fast != slow) {
                fast = nums[fast];
                slow = nums[slow];
            }
            return slow;
        }
        return -1;
    }

    int findDuplicate2(vector<int>& nums) {
        int l = 1, r = nums.size() - 1;
        while (l < r) {
            int m = (l + r) / 2, n = 0;
            for (int num : nums)
                n += num <= m;

            n <= m ? l = m + 1 : r = m;
        }
        return l;
    }
};