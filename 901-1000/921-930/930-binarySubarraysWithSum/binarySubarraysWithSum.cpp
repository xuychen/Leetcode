class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int sum = 0;
        unordered_map<int, int> count;
        int result = 0;
        for (int num : nums) {
            count[sum]++;
            sum += num;
            result += count[sum - goal];
        }
        return result;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/binary-subarrays-with-sum/solution/he-xiang-tong-de-er-yuan-zi-shu-zu-by-le-5caf/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。