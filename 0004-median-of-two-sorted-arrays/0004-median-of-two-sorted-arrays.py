class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array = nums1 + nums2
        merged_array.sort()
        n = len(merged_array)
        if n % 2 == 1:
            return float(merged_array[n // 2])
        else:
            mid = n // 2
            return (merged_array[mid - 1] + merged_array[mid]) / 2.0
        