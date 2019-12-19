#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> hashTable;
        int i = 0, startIndex = 0, length = 0;

        for (; i < s.size(); ++i) {
            auto value = hashTable.find(s[i]);
            if (value != hashTable.end() && startIndex <= value->second) {
                length = max(length, i-startIndex);
                startIndex = value->second + 1;
            }
            
            hashTable[s[i]] = i;
        }
        
        return max(length, i - startIndex);
    }
};