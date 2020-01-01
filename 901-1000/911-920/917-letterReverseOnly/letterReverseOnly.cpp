#include <string>

using namespace std;

class Solution {
public:
    string reverseOnlyLetters(string s) {
        string result;

        for (auto it: s)
            if (isalpha(it))
                result.push_back('c');
            else
                result.push_back(it);

        size_t index = 0;
        for (string::reverse_iterator riter = s.rbegin(); riter != s.rend(); ++riter)
            if (isalpha(*riter)) {
                while (result[index] != 'c')
                    ++index;

                result[index++] = *riter;
            }

        return result;
    }
};