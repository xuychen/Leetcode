#include <vector>

using namespace std;

class Solution {
public:
    int maximumElementAfterDecrementingAndRearranging(vector<int> &arr) {
        int n = arr.size();
        vector<int> cnt(n + 1);
        for (int v : arr) {
            ++cnt[min(v, n)];
        }
        
        int miss = 0;
        for (int i = 1; i <= n; ++i) {
            if (cnt[i] == 0) {
                ++miss;
            } else {
                miss -= min(cnt[i] - 1, miss); // miss 不会小于 0，故至多减去 miss 个元素
            }
        }
        return n - miss;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging/solution/jian-xiao-he-zhong-xin-pai-lie-shu-zu-ho-mzee/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。