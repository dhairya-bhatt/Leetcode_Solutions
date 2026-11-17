# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        sumlist = []
        while head:
            sumlist.append(head.val)
            head = head.next
        n = len(sumlist)
        maxi = 0
        for i in range(n // 2):
            maxi = max(maxi, sumlist[i] + sumlist[n - 1 - i])
        return maxi
