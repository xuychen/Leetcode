#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int partitionDisjoint(vector<int>& a) {
        vector<int> minVector(a);
        for (int i = a.size() - 2; i >= 0; --i)
            minVector[i] = min(minVector[i], minVector[i+1]);

        for (int i = 0, maxValue = a[i]; i < a.size() - 1; maxValue = max(maxValue, a[++i]))
            if (maxValue <= minVector[i+1])
                return i + 1;

        return 0;
    }
};