#include <vector>

using namespace std;

long getIdealNums(long low, long high) {
    vector<int> nums = {1};
    int c3 = 0, c5 = 0;
    int count = (low == 1);

    while (nums[nums.size()-1] <= high) {
        int next = min(3*nums[c3], 5*nums[c5]);
        nums.push_back(next);

        if (next == 3 * nums[c3])
            ++c3;
        if (next == 5 * nums[c5])
            ++c5;
        if (next >= low && next <= high)
            ++count;
    }

    return count;
}
