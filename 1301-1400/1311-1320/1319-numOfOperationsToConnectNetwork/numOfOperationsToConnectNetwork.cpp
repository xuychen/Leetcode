#include <vector>
#include <unordered_set>

using namespace std;

class UnionFind {
    vector<int> lists;
public:
    UnionFind(int size);
    bool merge(int x, int y);
    int find(int index);
    int getUnconnected();
};

UnionFind::UnionFind(int size) {
    for (int i = 0; i < size; ++i)
        lists.push_back(i);
}

bool UnionFind::merge(int x, int y) {
    if (lists[find(x)] == find(y))
        return false;

    lists[find(x)] = find(y);
    return true;
}

int UnionFind::find(int index) {
    return lists[index] == index ? index : find(lists[index]);
}

int UnionFind::getUnconnected() {
    unordered_set<int> hashSet;
    for (auto it: lists)
        hashSet.emplace(find(it));
    return hashSet.size();
}

class Solution {
public:
    int makeConnected(int n, vector<vector<int>>& connections) {
        UnionFind uf = UnionFind(n);
        int count = 0, unconnected = 0;

        for (auto &pair: connections)
            count += uf.merge(pair[0], pair[1]);

        unconnected = uf.getUnconnected();
        return count >= unconnected ? unconnected : -1;
    }
};