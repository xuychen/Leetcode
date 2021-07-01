#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (target == 100000)
            return -1;

        unordered_map<int, vector<int>> hashRoutes;

        for (int i = 0; i < routes.size(); ++i)
            for (int j = 0; j < routes[i].size(); ++j)
                hashRoutes[routes[i][j]].push_back(i);

        queue<pair<int, int>> qe;
        unordered_set<int> visited;
        qe.push(make_pair(source, 0));
        while (!qe.empty()) {
            auto pair = qe.front();
            qe.pop();
            int node = pair.first, count = pair.second;
            if (visited.find(node) == visited.end()) {
                if (node == target)
                    return count;

                for (int nextBus: hashRoutes[node])
                    for (int nextNode: routes[nextBus])
                        qe.push(make_pair(nextNode, count+1));

                visited.insert(node);
            }
        }

        return -1;
    }
};