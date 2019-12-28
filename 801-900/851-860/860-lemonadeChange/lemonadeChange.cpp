#include <vector>

using namespace std;

class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int changes[] = {0, 0};

        for (auto &it: bills)
            switch (it) {
                case 5: {
                    ++changes[0];
                    break;
                }
                case 10: {
                    if (!changes[0])
                        return false;

                    --changes[0];
                    ++changes[1];
                    break;
                }
                case 20: {
                    if (changes[1] && changes[0]) {
                        --changes[1];
                        --changes[0];
                    }
                    else if (changes[0] >= 3)
                        changes[0] -= 3;
                    else
                        return false;

                    break;
                }
                default:
                    break;
            }

        return true;
    }
};