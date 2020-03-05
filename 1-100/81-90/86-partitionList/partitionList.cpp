
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode *end = NULL, *greaterHead = NULL, *greaterEnd = NULL;

        for (ListNode *lptr = head; lptr; lptr = lptr->next) {
            if (lptr->val < x) {
                if (end)
                    end = end->next = lptr;
                else
                    head = end = lptr;
            }
            else {
                if (greaterEnd)
                    greaterEnd = greaterEnd->next = lptr;
                else
                    greaterHead = greaterEnd = lptr;
            }
        }

        if(greaterEnd)
            greaterEnd->next = NULL;
        if(end)
            end->next = greaterHead;

        return head;
    }
};