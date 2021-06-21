#include <list>
#include <queue>

class Solution {
public:
    list<int>::iterator orderedInsert(list<int>& linkedlist, int value) {
        list<int>::iterator iter;
        for (iter = linkedlist.begin(); *iter < value && iter != linkedlist.end(); ++iter);
        linkedlist.insert(iter, value);
        return --iter;
    }

    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        queue<list<int>::iterator> qe;
        list<int> linkedlist;
        vector<int> result;
        int i;

        for (i = 0; i < k - 1; ++i)
            qe.push(orderedInsert(linkedlist, nums[i]));

        for (; i < nums.size(); ++i) {
            qe.push(orderedInsert(linkedlist, nums[i]));
            result.push_back(linkedlist.back());
            linkedlist.erase(qe.front());
            qe.pop();
        }

        return result;
    }
};