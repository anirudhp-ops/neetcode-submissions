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
    bool hasCycle(ListNode* head) {
        ListNode* marker = new ListNode(-1); 
        
        while (head) {
            
            if ( head -> next == marker) {
                return true; 
            }
            else if ( head -> next == nullptr) {
                return false; 
            }
            ListNode* nextval = head -> next; 
            head -> next = marker; 
            head = nextval; 
        }
        return false; 
    }
};
