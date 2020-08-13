#include <string>
#include <vector>
#include <unordered_map>
#include <map>

using namespace std;

class Solution {
public:
    int strangePrinter(string s) {
        string unique;
        map<pair<int, int>, unordered_map<char, int>> dp;

        unique.push_back(s[0]);

        for (int i = 1; i < s.size(); ++i)
            if (s[i] != unique.back())
                unique.push_back(s[i]);

        int length = unique.size();

        for (int i = 0; i <= length; ++i){
            dp[pair(length-i, length)][' '] = length - 1;
            dp[pair(0, i)][' '] = length - 1;
        }

        for (int i = 1; i < length; ++i) {
            for (int j = length - 1; j >= i; --j) {
                auto range = dp[pair(i-1, j)];
                for (auto iter = range.begin(); iter != range.end(); ++iter)
                    dp[pair(i, j)][iter->first] = iter->second + (unique[i-1] != iter->first);

                range = dp[pair(i, j+1)];
                for (auto iter = range.begin(); iter != range.end(); ++iter)
                    dp[pair(i, j)][iter->first] = min(dp[pair(i, j)][iter->first], iter->second + (unique[i-1] != iter->first));

                if (unique[i-1] == unique[j]){
                    range = dp[pair(i-1, j+1)];
                    dp[pair(i, j)].emplace(unique[i-1], length);
                    for (auto iter = range.begin(); iter != range.end(); ++iter)
                        dp[pair(i, j)][unique[i-1]] = min(dp[pair(i, j)][unique[i-1]], iter->second + (unique[i-1] != iter->first));
                }
            }
        }

        int result = length;
        for (int i = 0; i < length; ++i)
            for (auto &it: dp[pair(1,1)])
                result = min(result, it.second);

        return result;
    }
};