class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1

        maxP = nums.index(max(nums)) + 1
        minP = nums.index(min(nums)) + 1

        y1 = max(maxP, minP)                          # front only
        y2 = n - min(maxP, minP) + 1                   # back only
        y3 = min(maxP, minP) + (n - max(maxP, minP))+1   # front + back

        return min(y1, y2, y3)
            
        

        