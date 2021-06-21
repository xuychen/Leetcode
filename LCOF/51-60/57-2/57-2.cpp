#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> result;

        for (int length = int(sqrt(2*target)); length > 1; --length) {
            vector<int> subResult;
            if (length & 1) {
                if (target % length == 0)
                    for (int i = target / length - length / 2; i <= target / length + length / 2; ++i)
                        subResult.push_back(i);
            }
            else if (target % length == length / 2) {
                for (int i = target / length - length / 2 + 1; i <= target / length + length / 2; ++i)
                    subResult.push_back(i);
            }

            if (!subResult.empty())
                result.push_back(subResult);
        }

        return result;
    }
};