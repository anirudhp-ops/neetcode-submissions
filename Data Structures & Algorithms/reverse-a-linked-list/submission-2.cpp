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
        ListNode* lastnode = new ListNode(head->val); 
        ListNode* curr = lastnode; 
        head = head -> next; 
        while ( head) {
            ListNode* firstnode = new ListNode(head->val, curr); 
            curr = firstnode; 
            ListNode* delnode = head; 
            head = head -> next; 
            delete delnode; 
            
        }
        return curr;  
    }
};
