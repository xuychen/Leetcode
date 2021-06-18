#include <unordered_map>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> dictionary;
        int result = 0;
        int start = 0;

        for (int i = 0; i < s.size(); ++i) {
            auto iter = dictionary.find(s[i]);
            if (iter != dictionary.end() && iter->second >= start)
                start = iter->second + 1;

            dictionary[s[i]] = i;
            result = max(result, i - start + 1);
        }

        return result;
    }
};