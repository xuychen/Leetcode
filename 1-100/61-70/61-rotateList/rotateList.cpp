// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int count = 0;
        ListNode *end = NULL, *newHead = head, *newEnd = head;

        if (!head)
            return head;

        for (ListNode *lptr = head; lptr; end = lptr, lptr = lptr->next, ++count);
        for (int i = 0; i < count - k % count - 1; newEnd = newEnd->next, ++i);

        if (newEnd->next) {
            newHead = newEnd->next;
            newEnd->next = NULL;
            end->next = head;
        }

        return newHead;
    }
};