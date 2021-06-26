#include <unordered_map>

using namespace std;

class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> stot;
        unordered_map<char, char> ttos;

        for (int i = 0; i < s.size(); ++i) {
            stot.emplace(s[i], t[i]);
            ttos.emplace(t[i], s[i]);

            if (stot[s[i]] != t[i] || ttos[t[i]] != s[i])
                return false;
        }

        return true;
    }
};