#include <vector>

using namespace std;

class Solution {
public:
    vector<int> constructArr(vector<int>& a) {
        vector<int> result = vector<int>(a.size(), 1);

        for (int i = 1; i < a.size(); ++i)
            result[i] *= result[i-1] * a[i-1];

        for (int i = a.size()-2, tmp = 1; i >= 0; --i) {
            tmp *= a[i+1];
            result[i] *= tmp;
        }

        return result;
    }
};