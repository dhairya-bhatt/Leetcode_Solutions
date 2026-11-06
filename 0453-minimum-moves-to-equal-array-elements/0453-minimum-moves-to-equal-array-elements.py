class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        mini = min(nums)
        count = 0

        for x in nums:
            count+= (x-mini)
        return count
