class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        if mini & 1:
            return True
        else:
            if all(num % 2 == 0 for num in nums1):
                return True
        return False
            