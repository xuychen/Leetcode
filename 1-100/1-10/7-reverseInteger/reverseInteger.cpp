#include <string>
#include <exception>

using namespace std;

class Solution {
public:
    int reverse(int x) {
        string s = to_string(x);
        if (s[0] == '-')
            ::reverse(s.begin()+1, s.end());
        else
            ::reverse(s.begin(), s.end());
        
        try {
            return stoi(s);
        } catch(exception& e) {
            return 0;
        }
    }
};