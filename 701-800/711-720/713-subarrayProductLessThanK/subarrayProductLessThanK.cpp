#include <vector>

using namespace std;

class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int start = 0, end = 0;
        int result = 0, value = nums[start];

        for (; end < nums.size() - 1;) {
            if (value < k) {
                result += end - start + 1;
                value *= nums[++end];
            }
            else {
                value /= nums[start];
                if (++start > end)
                    value *= nums[++end];
            }
        }

        while (value >= k && end >= start)
            value /= nums[start++];

        return result + (end - start + 1);
    }

    int numSubarrayProductLessThanK2(vector<int>& nums, int k) {
        int start = 0, end = 0;
        int result = 0, value = nums[start];

        for (; end < nums.size();) {
            if (value < k) {
                result += end - start + 1;
                value *= nums[++end];
            }
            else {
                value /= nums[start];
                if (++start > end)
                    value *= nums[++end];
            }
        }

        return result;
    }

    int numSubarrayProductLessThanK3(vector<int>& nums, int k) {
        int result = 0;
        for (int start = 0, end = 0, value = 1; end < nums.size(); ++end) {
            value *= nums[end];
            while (value >= k && end >= start)
                value /= nums[start++];

            result += end - start + 1;
        }

        return result;
    }
};