#include <unordered_map>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    string reorganizeString(string s) {
        unordered_map<char, int> counter;
        multimap<int, char> generator;
        string result;

        for (auto &it: s) {
            counter.emplace(it, 0);
            counter[it] += 1;
        }

        for (auto &it: counter)
            generator.insert(pair<int, char>(it.second, it.first));

        int key = generator.rbegin()->first;
        if (key > (s.size() + 1) / 2)
            return result;

        while (key > 0) {
            int count = 0;
            multimap<int, char>::reverse_iterator riter = generator.rbegin();
            for (; riter != generator.rend() && riter->first == key ; ++riter, ++count)
                result += riter->second;

            multimap<int, char>::iterator iter = riter.base();
            if (count == 1 && riter->first) {
                result += riter->second;
                generator.insert(pair<int, char>(riter->first-1, riter->second));
                generator.erase((++riter).base());
            }

            while (iter != generator.end() && iter->first == key) {
                generator.insert(pair<int, char>(key-1, iter->second));
                generator.erase(iter++);
            }

            key = generator.rbegin()->first;
        }

        return result;
    }

    string reorganizeString2(string S) {
        vector<int> mp(26);
        int n = S.size();
        for (char c: S) ++mp[c-'a'];
        vector<pair<int, char>> charCounts;
        for (int i = 0; i < 26; ++i) {
            if (mp[i] > (n+1)/2) return "";
            if (mp[i]) charCounts.push_back({mp[i], i+'a'});
        }
        sort(charCounts.rbegin(), charCounts.rend());
        string strSorted;
        for (auto& p: charCounts)
            strSorted += string(p.first, p.second);
        string ans;
        for (int i = 0, j = (n-1)/2+1; i <= (n-1)/2; ++i, ++j) {
            ans += strSorted[i];
            if (j < n) ans += strSorted[j];
        }
        return ans;
    }
};