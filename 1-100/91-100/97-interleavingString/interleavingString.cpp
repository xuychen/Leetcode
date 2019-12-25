#include <string>

using namespace std;

class Solution {
public:
    bool isInterleave(string s1, string s2, string s3) {
        size_t s1Length = s1.size(), s2Length = s2.size();

        if (s1Length + s2Length != s3.size())
            return false;

        bool **dp = new bool*[s1Length+1];
        for (size_t i = 0; i <= s1Length; ++i)
            dp[i] = new bool[s2Length+1];

        dp[0][0] = true;

        for (size_t i = 1; i <= s1Length; ++i)
            dp[i][0] = dp[i-1][0] && s1[i-1] == s3[i-1];
        for (size_t j = 1; j <= s2Length; ++j)
            dp[0][j] = dp[0][j-1] && s2[j-1] == s3[j-1];

        for (size_t i = 1; i <= s1Length; ++i)
            for (size_t j = 1; j <= s2Length; ++j)
                dp[i][j] = (dp[i-1][j] && s1[i-1] == s3[i+j-1]) || (dp[i][j-1] && s2[j-1] == s3[i+j-1]);

        return dp[s1Length][s2Length];
    }

    bool isInterleaveLessSpace(string s1, string s2, string s3) {
        size_t s1Length = s1.size(), s2Length = s2.size();

        if (s1Length + s2Length != s3.size())
            return false;

        bool *dp = new bool[s2Length+1];

        dp[0] = true;
        for (size_t i = 1; i <= s2Length; ++i)
            dp[i] = dp[i-1] && s2[i-1] == s3[i-1];

        for (size_t i = 1; i <= s1Length; ++i) {
            dp[0] &= s1[i-1] == s3[i-1];
            for (size_t j = 1; j <= s2Length; ++j)
                dp[j] = (dp[j] && s1[i-1] == s3[i+j-1]) || (dp[j-1] && s2[j-1] == s3[i+j-1]);
        }

        return dp[s2Length];
    }
};