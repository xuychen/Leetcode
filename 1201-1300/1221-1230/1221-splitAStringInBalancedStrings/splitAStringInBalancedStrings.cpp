class Solution {
public:
    int balancedStringSplit(string s) {
        int count = 0;
        int result = 0;

        for (auto chr: s) {
            if (chr == 'L')
                --count;
            else
                ++count;

            if (count == 0)
                ++result;
        }

        return result;
    }
};