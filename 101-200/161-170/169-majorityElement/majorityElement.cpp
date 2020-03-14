#include <vector>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> hashMap;
        int size = nums.size();

        for (auto it: nums) {
            hashMap.emplace(it, 0);
            hashMap[it] += 1;
        }

        for (auto it: hashMap)
            if (it.second > size / 2)
                return it.first;

        return -1;
    }

    // Boyer-Moore Majority Vote Algorithm
    // http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
    int BoyerMooreMajorityVote(vector<int>& nums) {
        int major = num[0], count = 1;
        for (auto it: nums)
            if (count == 0) {
                ++count;
                major = it;
            }
            else if (major == num[i])
                ++count;
            else
                --count;

        return major;
    }
};