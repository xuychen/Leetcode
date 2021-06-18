class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        int xor_result = 0;
        int pivot;
        vector<int> result = {0,0};

        for (int num: nums)
            xor_result ^= num;

        for (pivot = 1; !(xor_result & pivot); pivot <<= 1);
        for (int num: nums)
            result[!(num&pivot)] ^= num;

        return result;
    }
};