#include <queue>

using namespace std;

struct Cmp {
    bool operator() (pair<int, int> lhs, pair<int, int> rhs) {
        return lhs.first == rhs.first ? lhs.second < rhs.second : lhs.first < rhs.first;
    }
};

class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        priority_queue<pair<int, int> , vector<pair<int, int>>, Cmp> heapq;
        vector<int> result;
        int i;

        for (i = 0; i < k - 1; ++i)
            heapq.push(make_pair(nums[i], i));

        for (; i < nums.size(); ++i) {
            heapq.push(make_pair(nums[i], i));
            while (!heapq.empty() && heapq.top().second <= i - k)
                heapq.pop();

            result.push_back(heapq.top().first);
        }

        return result;
    }
};