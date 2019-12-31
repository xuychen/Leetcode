#include <algorithm>
#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int subarraysWithKDistinct(vector<int>& a, int k) {
        unordered_map<int, int> hashTable;
        int left = 0, index = 0, result = 0;

        for (; index < a.size(); ++index) {
            hashTable[a[index]] = index;
            int size = hashTable.size();

            if (size > k) {
                int minIndex = index;
                for (auto &it: hashTable)
                    minIndex = min(minIndex, it.second);

                hashTable.erase(a[minIndex]);
                left = minIndex + 1;
            }

            if (size == k) {
                int minIndex = index;
                for (auto &it: hashTable)
                    minIndex = min(minIndex, it.second);

                result += minIndex - left + 1;
            }
        }

        return result;
    }

    int subarraysWithKDistinct2(vector<int>& A, int K) {
        return atMostK(A, K) - atMostK(A, K - 1);
    }

    int atMostK(vector<int>& A, int K) {
        int i = 0, res = 0;
        unordered_map<int, int> count;
        for (int j = 0; j < A.size(); ++j) {
            if (!count[A[j]]++) K--;
            while (K < 0) {
                if (!--count[A[i]]) K++;
                i++;
            }
            res += j - i + 1;
        }
        return res;
    }

    int subarraysWithKDistinct3(vector<int>& A, int K, int res = 0) {
        vector<int> m(A.size() + 1);
        for(auto i = 0, j = 0, prefix = 0, cnt = 0; i < A.size(); ++i) {
            if (m[A[i]]++ == 0) ++cnt;
            if (cnt > K) --m[A[j++]], --cnt, prefix = 0;
            while (m[A[j]] > 1) ++prefix, --m[A[j++]];
            if (cnt == K) res += prefix + 1;
        }
        
        return res;
    }
};