#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    vector<string> permutation(string s) {
        if (s.empty())
            return vector<string>(1, "");

        vector<string> result;
        unordered_set<char> visited;

        for (int i = 0; i < s.size(); visited.insert(s[i++]))
            if (visited.find(s[i]) == visited.end())
                for (string &elem: permutation(s.substr(0, i)+s.substr(i+1, s.size()-i-1)))
                    result.push_back(s[i]+elem);

        return result;
    }
};