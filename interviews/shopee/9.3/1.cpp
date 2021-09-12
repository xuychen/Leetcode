#include <unordered_map>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    /**
     * Note: 类名、方法名、参数名已经指定，请勿修改
     *
     * 
     * 
     * @param inputStr string字符串 Input string
     * @return int整型
     */
    int getMaxSubstrLenProd(string inputStr) {
        // write code here
        int length = inputStr.size();
        unordered_map<string, int> dictionary;
        string dp[length][length];

        for (int i = 0; i < length; ++i) {
            string s = "";
            s.push_back(inputStr[i]);
            s.push_back(inputStr[i]);
            dp[i][i] = s;
        }

        for (int i = 0; i < length; ++i) {
            for (int j = i+1; j < length; ++j) {
                if (dp[i][j-1][0] > inputStr[j]) {
                    string s = "";
                    s.push_back(inputStr[j]);
                    s.push_back(dp[i][j-1][1]);
                    dp[i][j] = s;
                }    
                else if (dp[i][j-1][1] < inputStr[j]) {
                    string s = "";
                    s.push_back(dp[i][j-1][0]);
                    s.push_back(inputStr[j]);
                    dp[i][j] = s;
                }
                else {
                    dp[i][j] = dp[i][j-1];
                }

                dictionary[dp[i][j]] = max(dictionary[dp[i][j]], j - i + 1);
            }
        }

        int result = 0;
        for (auto &it1: dictionary) {
            for (auto &it2: dictionary) {
                if (it1.first[0] > it2.first[1] || it2.first[0] > it1.first[1])
                    result = max(result, it1.second * it2.second);
            } 
        }

        return result;
    }
};

int main() {
    Solution s = Solution();
     cout << s.getMaxSubstrLenProd("adcbadcbedbadedcbacbcadbc") << endl;
} 