#include <vector>

using namespace std;

class Solution {
public:
    int candy(vector<int>& ratings) {
        vector<int> candies (ratings.size(), 1);

        // from left to right
        for (int i = 1; i < ratings.size(); ++i) {
            if (ratings[i] > ratings[i-1] && candies[i] <= candies[i-1])
                candies[i] = candies[i-1] + 1;
            else if (ratings[i] < ratings[i-1] && candies[i] >= candies[i-1])
                candies[i-1] = candies[i] + 1;
        }

        // from right to left
        for (int j = ratings.size()-2; j >= 0; --j) {
            if (ratings[j] > ratings[j+1] && candies[j] <= candies[j+1])
                candies[j] = candies[j+1] + 1;
            else if (ratings[j] < ratings[j+1] && candies[j] >= candies[j+1])
                candies[j+1] = candies[j] + 1;
        }

        return accumlate(candies.begin(), candies.end(), 0);
    }
}

class Solution2 {
public:
    int candy(vector<int>& ratings) {
        int n = ratings.size();
        vector<int> left(n);
        for (int i = 0; i < n; i++) {
            if (i > 0 && ratings[i] > ratings[i - 1]) {
                left[i] = left[i - 1] + 1;
            } else {
                left[i] = 1;
            }
        }
        int right = 0, ret = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (i < n - 1 && ratings[i] > ratings[i + 1]) {
                right++;
            } else {
                right = 1;
            }
            ret += max(left[i], right);
        }
        return ret;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/candy/solution/fen-fa-tang-guo-by-leetcode-solution-f01p/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。