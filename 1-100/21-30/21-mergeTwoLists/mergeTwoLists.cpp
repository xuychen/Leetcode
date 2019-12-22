#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
        ListNode *head = NULL;
        ListNode *prev = NULL;

        while (l1 && l2) {
            if (l1->val < l2->val) {
                ListNode *next = l1->next;
                if (prev)
                    prev = prev->next = l1;
                else
                    head = prev = l1;

                l1 = next;
            } else {
                ListNode *next = l2->next;
                if (prev)
                    prev = prev->next = l2;
                else
                    head = prev = l2;

                l2 = next;
            }
        }

        if (!l1)
            l1 = l2;

        if (prev)
            prev->next = l1;
        else
            head = l1;

        return head;
    }

    ListNode *mergeTwoListsToNew(ListNode *l1, ListNode *l2) {
        ListNode *head = NULL, *prev = NULL;
        int value;

        while (l1 && l2) {
            if (l1->val < l2->val) {
                value = l1->val;
                l1 = l1->next;
            }
            else {
                value = l2->val;
                l2 = l2->next;
            }

            if (prev)
                prev = prev->next = new ListNode(value);
            else
                head = prev = new ListNode(value);
        }

        if (!l1)
            l1 = l2;

        for (; l1; l1 = l1->next)
            if (prev)
                prev = prev->next = new ListNode(l1->val);
            else
                head = prev = new ListNode(l1->val);

        return head;
    }
};