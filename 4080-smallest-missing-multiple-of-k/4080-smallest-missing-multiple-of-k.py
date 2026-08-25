class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        multiples = k
        for i in range(len(nums)+6):
            if multiples not in nums:
                return multiples
            else:
                multiples += k
        
        