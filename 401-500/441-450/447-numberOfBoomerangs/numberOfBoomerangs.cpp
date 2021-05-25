#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
    int numberOfBoomerangs(vector<vector<int> >& points) {
        int booms = 0;
        for (auto &p : points) {
            unordered_map<double, int> ctr(points.size());
            for (auto &q : points)
                booms += 2 * ctr[hypot(p[0] - q[0], p[1] - q[1])]++;
        }

        return booms;
    }
};