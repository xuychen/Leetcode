#include <vector>

using namespace std;

class Solution {
public:
    char firstUniqChar(string s) {
        vector<int> dictionary = vector<int>(26, -1);
        int min_index = s.size();
        char result = ' ';

        for (int i = 0; i < s.size(); ++i)
            if (dictionary[s[i] - 'a'] == -1)
                dictionary[s[i] - 'a'] = i;
            else if (dictionary[s[i] - 'a'] >= 0)
                dictionary[s[i] - 'a'] = -2;

        for (int i = 0; i < 26; ++i)
            if (dictionary[i] >= 0)
                min_index = min(min_index, dictionary[i]);

        if (min_index != s.size())
            result = s[min_index];

        return result;
    }
};