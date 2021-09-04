/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getKthFromEnd(struct ListNode* head, int k){
    struct ListNode *fast = head, *slow = head;
    int i = 0;
    while (i++ < k)
        fast = fast->next;

    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }

    return slow;
}