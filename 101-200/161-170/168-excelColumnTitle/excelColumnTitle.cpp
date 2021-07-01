#include <string>

using namespace std;

class Solution {
public:
    string convertToTitle(int columnNumber) {
        string result = "";
        for (; columnNumber-- > 0; columnNumber /= 26)
            result += 'A' + columnNumber % 26;

        reverse(result.begin(), result.end());
        return result;
    }
};