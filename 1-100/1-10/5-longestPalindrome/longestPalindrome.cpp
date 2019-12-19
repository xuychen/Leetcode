#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        // Manacher Algorithm
        string newS = "$";
        vector<int> pArray;
        int center = 0, maxRight = 0, resultCenter = 0, resultLength = 0;

        for (auto &it: s){
            newS.push_back('#');
            newS.push_back(it);
        }

        newS.push_back('#');
        pArray.push_back(0);
    
        for (int index = 1; index <= s.size() * 2; ++index) {
            int next = index < maxRight ? min(pArray[2*center-index], maxRight-index) : 1;
            pArray.push_back(next);
            while (newS[index + pArray[index]] == newS[index - pArray[index]]) ++pArray[index];
            
            if (maxRight < index + pArray[index]) {
                maxRight = index + pArray[index];
                center = index;
            }
            
            if (resultLength < pArray[index]) {
                resultLength = pArray[index];
                resultCenter = index;
            }
        }
    
        return s.substr((resultCenter - resultLength) / 2, resultLength - 1);
    }

    string longestPalindrome2(string s) {
        string newS;
        int maxLeft = 0, maxLength = 0;

        if (s.size() <= 1)
            return s;

        for (auto &it: s){
            newS.push_back(it);
            newS.push_back('#');
        }

        newS.pop_back();

        for (size_t i = 0; i < newS.size(); ++i) {
            for (size_t radius = 0; radius <= i; ++radius) {
                if (newS[i-radius] != newS[i+radius])
                    break;
                
                if (newS[i] == '#') {
                    if (maxLength < (radius+1)/2*2) {
                        maxLength = (radius + 1) / 2 * 2;
                        maxLeft = i - radius;
                    }
                }
                else {
                    if (maxLength < radius/2*2+1) {
                        maxLength = radius / 2 * 2 + 1;
                        maxLeft = i - radius;
                    }
                }
            }
        }

        return s.substr((maxLeft+1)/2, maxLength);
    }
};