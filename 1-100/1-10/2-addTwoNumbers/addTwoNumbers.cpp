/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */

// for get rid of compiling errors
#include <iostream>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

// answer below
class Solution {
   public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
        ListNode *l1ptr = l1;
        ListNode *l2ptr = l2;
        ListNode *l3ptr;
        ListNode *head = NULL;
        int carryOn = 0;

        while (l1ptr != NULL || l2ptr != NULL || carryOn != 0) {
            int num1, num2;

            if (l1ptr == NULL)
                num1 = 0;
            else {
                num1 = l1ptr->val;
                l1ptr = l1ptr->next;
            }

            if (l2ptr == NULL)
                num2 = 0;
            else {
                num2 = l2ptr->val;
                l2ptr = l2ptr->next;
            }

            int result = num1 + num2 + carryOn;
            carryOn = result / 10;
            result %= 10;

            if (head == NULL)
                l3ptr = head = new ListNode(result);
            else
                l3ptr = l3ptr->next = new ListNode(result);
        }

        return head;
    }

    ListNode* addTwoNumbers2(ListNode* l1, ListNode* l2) {
        ListNode *prev = NULL;
        ListNode *head = NULL;
        int carryOn = 0;
        int l1value, l2value;
        
        while (l1 || l2) {
            l1value = l2value = 0;
            if (l1) {
                l1value = l1->val;
                l1 = l1->next;
            }
            if (l2) {
                l2value = l2->val;
                l2 = l2->next;
            }
            
            int value = l1value + l2value + carryOn;
            carryOn = value / 10;
            value -= carryOn * 10;
            
            ListNode *newNode = new ListNode(value);
            if (prev)
                prev = prev->next = newNode;
            else
                head = prev = newNode;
        }
        
        if (carryOn)
            prev->next = new ListNode(carryOn);
        
        return head;
    }
};