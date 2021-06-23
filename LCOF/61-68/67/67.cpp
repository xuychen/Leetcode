#include <climits>

class Solution {
public:
    int strToInt(string str) {
        int i;
        long result = 0;
        bool negative = false;
        for (i = 0; str[i] == ' ' && i < str.size(); ++i);

        if (i < str.size() && (str[i] == '+' || str[i] == '-'))
            negative = str[i++] == '-';

        for (; i < str.size() && isdigit(str[i]); ++i)
            if (result * 10 + str[i] - '0' > INT_MAX)
                return negative ? INT_MIN : INT_MAX;
            else
                result = result * 10 + str[i] - '0';

        return (negative ? -1 : 1) * result;
    }
};