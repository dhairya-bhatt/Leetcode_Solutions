# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: ListNode | None) -> list[int]:
        ans = []
        ind=[]
        vals=[]
        i=0
        while head is not None:
            while ind and vals[ind[-1]] < head.val:
                ans[ind.pop()] = head.val

            ans.append(0)
            vals.append(head.val)
            ind.append(i)

            i += 1
            head = head.next
        return ans