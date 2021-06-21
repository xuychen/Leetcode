#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    vector<double> dicesProbability(int n) {
        unordered_map<int, int> curr_map = {{0, 1}};
        unordered_map<int, int> next_map;
        double total = pow(6, n);
        vector<double> result;
        result.resize(5*n+1);

        for (int i = 0; i < n; ++i) {
            next_map.clear();
            for (unordered_map<int, int>::iterator iter = curr_map.begin(); iter != curr_map.end(); ++iter)
                for (int j = 1; j <= 6; ++j) {
                    next_map.emplace(iter->first+j, 0);
                    next_map[iter->first+j] += iter->second;
                }

            curr_map = next_map;
        }

        for (unordered_map<int, int>::iterator iter = curr_map.begin(); iter != curr_map.end(); ++iter)
            result[iter->first-n] = iter->second / total;

        return result;
    }
};