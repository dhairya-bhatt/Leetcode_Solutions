# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        def reverse(left,right, cur):
            node=None
            rev=cur
            while cur and left<=right:
                tmp=cur.next
                cur.next=node
                node=cur
                left+=1
                cur=tmp
            rev.next=cur
            return node
        if not head or not head.next or left==right:
            return head
        curr=head
        prev=head
        n=1
        while curr:
            if left==1 and n==1:
                head=reverse(left,right,curr)
            elif n==left:
                prev.next=reverse(left,right,curr)
            prev=curr
            curr=curr.next
            n+=1
        return head