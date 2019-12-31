#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
   int minIncrementForUnique(vector<int>& a) {
        if (a.size() < 2)
            return 0;

        int count = 0, result = 0;

        sort(a.begin(), a.end());
        for (size_t i = 1; i < a.size(); ++i) {
            if (a[i-1] == a[i])
                ++count;
            else {
                int difference = a[i] -  a[i-1];
                int upperbound = count - difference + 1;

                if (count < difference) {
                    result += (1 + count) * count / 2;
                    count = 0;
                }
                else {
                    result += (upperbound + count) * difference / 2;
                    count = upperbound;
                }

            }
        }

        return result + (1 + count) * count / 2;
    }

    int minIncrementForUnique2(vector<int>& a) {
        if (a.size() < 2)
            return 0;

        map<int, int> hashTable;

        for (auto &it: a) {
            hashTable.emplace(it, -1);
            ++hashTable[it];
        }

        int result = 0;

        map<int, int>::iterator iter = ++hashTable.begin();
        map<int, int>::iterator prev = hashTable.begin();

        for (; iter != hashTable.end(); ++iter) {
            int difference = iter->first - prev->first;
            int upperbound = prev->second - difference + 1;

            if (prev->second < difference)
                result += (1 + prev->second) * prev->second / 2;
            else {
                result += (upperbound + prev->second) * difference / 2;
                iter->second += upperbound;
            }

            prev = iter;
        }

        return result + (1 + prev->second) * prev->second / 2;
    }

    int minIncrementForUnique3(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 0, need = 0;
        
        for (int a: A) {
            res += max(need - a, 0);
            need = max(a, need)+1;
        }
        return res;
    }
};