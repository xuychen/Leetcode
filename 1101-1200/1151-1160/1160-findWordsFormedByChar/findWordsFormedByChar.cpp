#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int result = 0;
        multiset<char> charSet(chars.begin(), chars.end());

        for (auto &it: words) {
            multiset<char> wordSet(it.begin(), it.end());
            if (includes(charSet.begin(), charSet.end(), wordSet.begin(), wordSet.end()))
                result += it.size();
        }

        return result;
    }
};