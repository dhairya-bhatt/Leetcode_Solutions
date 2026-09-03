class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mini = min(nums1)
        if mini & 1:
            return True
        else:
            for x in range(len(nums1)):
                if nums1[x] & 1:
                    return False
        return True
            