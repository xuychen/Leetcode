#include <vector>

using namespace std;

class Solution {
public:
    int numTrees(int n) {
        vector<int> result = vector<int> (n+1, 0);
        result[0] = result[1] = 1;
        
        for (int i = 2; i <= n; ++i)
            for (int j = 1; j <= i; ++j)
                result[i] += result[j-1] * result[i-j];
        
        return result.back();
    }
};