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
        
        ListNode* curr = head; 
        ListNode* prev = nullptr; 
        
        while (curr) {
            ListNode* next = curr -> next; // preserves the rest of the list
            curr -> next = prev; // attched the node to the reveresed list
            prev = curr; // moving down the list to update what needs to be attached
            curr = next; // continues the list
        }
        return prev; 
    }

};
