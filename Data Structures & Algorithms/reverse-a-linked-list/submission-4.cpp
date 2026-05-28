/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) {
            return nullptr; 
        }

        ListNode* lastnode = head; 
        head = head->next; 
        lastnode -> next = nullptr; 
        while(head) {
            ListNode* curr = new ListNode(head -> val, head -> next); 
            head -> next = lastnode; 
            lastnode = head; 
            head = curr -> next; 
            delete curr; 
        }
        return lastnode; 
    }
};
