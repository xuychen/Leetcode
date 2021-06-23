class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int low = INT_MAX, high = -INT_MAX;
        int result = 0;

        for (int num: prices) {
            if (num < low) {
                low = num;
                high = -INT_MAX;
            }
            if (num > high)
                high = num;

            result = max(high-low, result);
        }

        return result;
    }
};