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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* curr = head->next;
        ListNode* nextSum = curr;
        bool start = false;
        while(nextSum != nullptr){
            int sum = 0;
            while (nextSum->val !=0){
                sum+=nextSum->val;
                nextSum = nextSum->next;
            }
            curr->val=sum;
            nextSum = nextSum->next;
            curr->next = nextSum;
            curr = curr->next;
        }
        return head->next;
    }
};