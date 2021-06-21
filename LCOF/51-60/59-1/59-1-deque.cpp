#include <queue>

using namespace std;

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        deque<int> dq;
        vector<int> result;
        int i;

        for (i = 0; i < k; ++i) {
            while (!dq.empty() && nums[i] > dq.back())
                dq.pop_back();

            dq.push_back(nums[i]);
        }

        if (!dq.empty())
            result.push_back(dq.front());

        for (; i < nums.size(); ++i) {
            while (!dq.empty() && nums[i] > dq.back())
                dq.pop_back();

            dq.push_back(nums[i]);
            if (nums[i-k] == dq.front())
                dq.pop_front();

            result.push_back(dq.front());
        }

        return result;
    }
};