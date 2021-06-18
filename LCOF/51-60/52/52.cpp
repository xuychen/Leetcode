/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        unordered_set<ListNode*> set;
        ListNode *nodeA = headA, *nodeB = headB;

        while (nodeA) {
            set.insert(nodeA);
            nodeA = nodeA->next;
        }

        while (nodeB && set.find(nodeB) == set.end())
            nodeB = nodeB->next;

        return nodeB;
    }

    // double pointer algorithm
    ListNode *getIntersectionNode2(ListNode *headA, ListNode *headB) {
        ListNode *nodeA = headA, *nodeB = headB;

        while (nodeA != nodeB) {
            nodeA = nodeA ? nodeA->next : headB;
            nodeB = nodeB ? nodeB->next : headA;
        }

        return nodeA;
    }
};