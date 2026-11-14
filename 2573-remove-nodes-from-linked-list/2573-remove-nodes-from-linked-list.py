# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: ListNode | None) -> ListNode | None:
        def reverseList(head):
            prev = None
            cur = head
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur=temp
            return prev
        
        
        reverselist = reverseList(head)

        currMax = None
        prev =None
        curr = reverselist
        while curr:
            if not prev:
                currMax=curr.val
                prev=curr
                curr=curr.next
            
            else:

                if(curr.val>=currMax):
                    currMax=curr.val
                    prev=curr
                    curr=curr.next
                
                else:
                    prev.next=curr.next
                    curr=curr.next
        

        return reverseList(reverselist)


        