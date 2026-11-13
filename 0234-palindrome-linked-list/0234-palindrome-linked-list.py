# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        templist = []
        while (head):
            templist.append(head.val)
            head = head.next
        

        return templist == templist[::-1]