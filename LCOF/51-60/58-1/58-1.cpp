#include <vector>

using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        vector<string> result;
        s += " ";

        for (int i = 0, start = -1; i < s.size(); ++i) {
            if (s[i] != ' '){
                if (start == -1)
                    start = i;
            }
            else if (start != -1) {
                result.push_back(s.substr(start, i - start));
                start = -1;
            }
        }

        return result.empty() ? "" : accumulate(result.rbegin()+1, result.rend(), result[result.size()-1], [](string lhs, string rhs) -> string { return lhs + " " + rhs; });
    }
};