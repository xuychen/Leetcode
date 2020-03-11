#include <algorithm>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* sortList(ListNode* list) {
        ListNode *ptr, *double_ptr, *prev;

        if (!list || !list->next)
            return list;
        
        for (ptr = list, double_ptr = list, prev = NULL; double_ptr && double_ptr->next; 
                                prev = ptr, ptr = ptr->next, double_ptr = double_ptr->next->next);
        
        prev->next = NULL;
        ListNode *sortedLeft = sortList(list);
        ListNode *sortedRight = sortList(ptr);
        ListNode *head = NULL, *end = NULL;
        
        while (sortedLeft && sortedRight)
            if (sortedLeft->val < sortedRight->val) {
                if (head)
                    end = end->next = sortedLeft;
                else
                    head = end = sortedLeft;

                sortedLeft = sortedLeft->next;
            }
            else {
                if (head)
                    end = end->next = sortedRight;
                else
                    head = end = sortedRight;

                sortedRight = sortedRight->next;
            }

        
        end->next = sortedLeft ? sortedLeft : sortedRight;
        return head;
    }
};