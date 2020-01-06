#include <vector>
#include <queue>
#include <functional>

using namespace std;

typedef pair<int, int> QueueItem;

template <class T>
struct Comp {
    bool operator() (const T& lhs, const T& rhs) const{
        return lhs.first > rhs.first;
    }
};

class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        priority_queue<QueueItem, vector<QueueItem>, Comp<QueueItem>> queue;
        size_t size = matrix.size();
        vector<int> indices = vector<int>(size, 0);

        for (int i = 0; i < size; ++i)
            queue.push({matrix[i][0], i});

        for (int i = 1; i < k; ++i) {
            int index = queue.top().second;
            queue.pop();

            if (++indices[index] < size)
                queue.push({matrix[index][indices[index]], index});
        }

        return queue.top().first;
    }
};