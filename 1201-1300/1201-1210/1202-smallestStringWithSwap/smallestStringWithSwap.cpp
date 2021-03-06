#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class UnionFind {
    unordered_map<int, int> unionSet;

public:
    UnionFind(){};
    void merge(int x, int y);
    int find(int x);
};

void UnionFind::merge(int x, int y) {
    unionSet[find(x)] = find(y);
}

int UnionFind::find(int x) {
    unionSet.emplace(x, x);
    return unionSet[x] == x ? x : find(unionSet[x]);
}

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        UnionFind uf;
        unordered_map<int, string> hashTable;
        string result;

        for (auto& pair : pairs)
            uf.merge(pair[0], pair[1]);
        for (int i = 0; i < s.size(); ++i)
            hashTable[uf.find(i)].push_back(s[i]);
        for (auto& it : hashTable)
            sort(it.second.begin(), it.second.end(), greater<char>());
        for (int i = 0; i < s.size(); ++i) {
            result.push_back(hashTable[uf.find(i)].back());
            hashTable[uf.find(i)].pop_back();
        }

        return result;
    }

    int find(vector<int>& ds, int i) {
        return ds[i] < 0 ? i : ds[i] = find(ds, ds[i]);
    }

    string smallestStringWithSwaps2(string s, vector<vector<int>>& pairs) {
        vector<int> ds(s.size(), -1);
        vector<vector<int>> m(s.size());
        for (auto& p : pairs) {
            auto i = find(ds, p[0]), j = find(ds, p[1]);
            if (i != j) {
                if (-ds[i] < -ds[j])
                    swap(i, j);
                ds[i] += ds[j];
                ds[j] = i;
            }
        }
        for (auto i = 0; i < s.size(); ++i) m[find(ds, i)].push_back(i);
        for (auto ids : m) {
            string ss = "";
            for (auto id : ids) ss += s[id];
            sort(begin(ss), end(ss));
            for (auto i = 0; i < ids.size(); ++i) s[ids[i]] = ss[i];
        }
        return s;
    }
};