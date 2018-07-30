/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
   public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        switch (lists.size()) {
            case 0:
                return NULL;
            case 1:
                return lists[0];
            default:
                return partition(lists, 0, lists.size() - 1);
        }
    }

    ListNode* partition(vector<ListNode*>& lists, int start, int end) {
        int middle = (start + end) / 2;
        if (start == end) return lists[start];
        return merge(partition(lists, start, middle),
                     partition(lists, middle + 1, end));
    }

    ListNode* merge(ListNode* left, ListNode* right) {
        if (!left) return right;
        if (!right) return left;

        if (left->val < right->val) {
            left->next = merge(left->next, right);
            return left;
        } else {
            right->next = merge(left, right->next);
            return right;
        }
    }
};