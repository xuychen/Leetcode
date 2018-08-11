// to get rid of compiling errors
#include <vector>
using namespace std;

// answer below
class Solution {
   public:
    int firstMissingPositive(vector<int> &nums) {
        for (int index = 0; index < nums.size(); index++) {
            int next = -1;  // start
            for (int jump = nums[index];
                 jump > 0 && jump <= nums.size() && jump != nums[jump - 1];
                 jump = next) {
                next = nums[jump - 1];
                nums[jump - 1] = jump;
            }
        }

        int index;
        for (index = 0; index < nums.size(); index++) {
            if (index + 1 != nums[index]) return index + 1;
        }

        return index + 1;
    }
};