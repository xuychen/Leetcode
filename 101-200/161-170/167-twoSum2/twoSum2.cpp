#include <vector>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int start = 1, end = numbers.size();

        while (start < end) {
            if (numbers[start-1] + numbers[end-1] > target)
                --end;
            else if (numbers[start-1] + numbers[end-1] < target)
                ++start;
            else
                return {start, end};
        }

        return vector<int> ();
    }
};