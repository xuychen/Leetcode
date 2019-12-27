#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int findPoisonedDuration(vector<int>& timeSeries, int duration) {
        int totalTime = 0;

        for (int i = 1; i < timeSeries.size(); ++i)
            totalTime += min(timeSeries[i] - timeSeries[i-1], duration);

        if (!timeSeries.empty())
            totalTime += duration;

        return totalTime;
    }
};