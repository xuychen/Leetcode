#include <string>
#include <cctype>

#define ASCII0 48

using namespace std;

class Solution {
public:
    int myAtoi(string str) {
        long num = 0;
        size_t i;
        bool isNegative = false;
        
        for (i = 0; str[i] == ' ' && i < str.size(); ++i);
        
        if (str[i] == '-') {
            isNegative = true;
            ++i;
        }
        else if (str[i] == '+')
            ++i;
        
        for (; i < str.size(); ++i)
            if (isdigit(str[i]) && num <= INT_MAX) {
                num *= 10;
                num += str[i] - ASCII0;
            }
            else
                break;
        
        return isNegative ? (-num < INT_MIN ? INT_MIN : -num) : (num > INT_MAX ? INT_MAX : num);
    }
};