#include <vector>
#include <unordered_set>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string vectorToString(vector<int>& nums) {
        string str;
        for (auto &it: nums)
            str.append(to_string(it) + " ");

        return str;
    }

    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> result;
        unordered_set<string> uniqueTable;

        sort(nums.begin(), nums.end());

        for (size_t i = 0; i < nums.size(); ++i) {
            unordered_set<int> hashTable;

            for (size_t j = i + 1; j < nums.size(); ++j) {
                int value = nums[i] + nums[j];
                auto iter = hashTable.find(-nums[j]);

                if (iter == hashTable.end())
                    hashTable.insert(value);
                else {
                    vector<int> newSet = {nums[i], *iter-nums[i], nums[j]};

                    if (uniqueTable.emplace(vectorToString(newSet)).second)
                        result.push_back(newSet);
                }
            }
        }

        return result;
    }
};