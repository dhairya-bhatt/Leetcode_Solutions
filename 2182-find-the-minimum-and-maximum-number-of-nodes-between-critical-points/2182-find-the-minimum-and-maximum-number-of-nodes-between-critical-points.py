# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def is_crit(first,second,third):
            return (second.val-first.val)*(second.val-third.val)>0

        prev = head
        cur = head.next
        nex = head.next.next
        min_dist = float('inf')

        first,last,idx = -1,-1,1
        while nex is not None:
            if is_crit(prev,cur,nex):
                if first ==-1:
                    first = idx
                    last=idx
                else:
                    min_dist = min(min_dist,idx-last)
                    last = idx
            prev = cur
            cur = nex
            nex = nex.next
            idx += 1

        if first == last:
            return[-1,-1]

        return [min_dist, last - first]
