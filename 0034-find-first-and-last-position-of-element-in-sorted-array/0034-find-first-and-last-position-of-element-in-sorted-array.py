class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def fL():
            l, r = 0, len(nums) - 1
            left = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
                if nums[m] == target:
                    left = m
            return left
        
        def fR():
            l, r = 0, len(nums) - 1
            right = -1
            while l <= r:
                m = (l + r) // 2
                if nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1
                if nums[m] == target:
                    right = m
            return right
        
        return [fL(), fR()]