#include <vector>

using namespace std;

class Solution {
public:
    int findSubstringInWraproundString(string p) {
        vector<int> letters(26, 0);
        int res = 0, len = 0;
        for (int i = 0; i < p.size(); ++i) {
            int cur = p[i] - 'a';
            char prev = cur ? cur - 1 + 'a' : 'z';
            if (i > 0 && p[i - 1] != prev)
                len = 0;
            if (++len > letters[cur]) {
                res += len - letters[cur];
                letters[cur] = len;
            }
        }

        return res;
    }
};