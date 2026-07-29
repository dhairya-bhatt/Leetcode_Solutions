# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        
        def listnode_to_list(head):
            result = []
            current = head
            while current:
                result.append(current.val)
                current = current.next
            return result
        resultl1 = listnode_to_list(l1)
        resultl2 = listnode_to_list(l2)


        reversel1 = resultl1[::-1]
        reversel2 = resultl2[::-1]
        # print(reversel1)
        reversel1num = ""
        reversel2num = ""
        for i in range(len(reversel1)):
                reversel1num += str(reversel1[i])
        for i in range(len(reversel2)):
                reversel2num += str(reversel2[i])
        sum = str(int(reversel1num) + int(reversel2num))
        
        dummy = ListNode(0)
        current = dummy
        for digit in reversed(sum):
            current.next = ListNode(int(digit))
            current = current.next

        return dummy.next
        
        
        