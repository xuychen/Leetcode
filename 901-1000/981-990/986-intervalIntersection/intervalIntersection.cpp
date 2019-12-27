#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& a, vector<vector<int>>& b) {
        size_t aIndex = 0, bIndex = 0;
        size_t aLength = a.size(), bLength = b.size();
        vector<vector<int>> result;

        while (aIndex < aLength && bIndex < bLength) {
            vector<int> aInterval = a[aIndex], bInterval = b[bIndex];
            int left, right;
            left = max(aInterval[0], bInterval[0]);

            if (aInterval[1] <= bInterval[1]) {
                ++aIndex;
                right = aInterval[1];
            }
            if (aInterval[1] >= bInterval[1]) {
                ++bIndex;
                right = bInterval[1];
            }

            if (left <= right)
                result.push_back({left, right});
        }

        return result;
    }

    vector<vector<int>> intervalIntersection2(vector<vector<int>>& a, vector<vector<int>>& b) {
        size_t aIndex = 0, bIndex = 0;
        size_t aLength = a.size(), bLength = b.size();
        vector<vector<int>> result;

        while (aIndex < aLength && bIndex < bLength) {
            int left = max(a[aIndex][0], b[bIndex][0]);
            int right = a[aIndex][1] <= b[bIndex][1] ? a[aIndex++][1] : b[bIndex++][1];

            if (left <= right)
                result.push_back({left, right});
        }

        return result;
    }
};