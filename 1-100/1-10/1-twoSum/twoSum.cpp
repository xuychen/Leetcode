#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;

class Solution {
  public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> result;
        unordered_map<int, int> hashTable;
        for (size_t i = 0; i < nums.size(); ++i) {
            auto value = hashTable.find(target-nums[i]);
            if (value != hashTable.end()) {
                result.push_back(value->second);
                result.push_back(i);
            }
            
            hashTable.insert(make_pair(nums[i], i));
        }
        
        return result;
    }
};