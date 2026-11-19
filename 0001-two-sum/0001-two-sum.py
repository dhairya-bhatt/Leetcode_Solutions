class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i,j in enumerate(nums):
            if target-j in seen:
                return [seen[target-j],i]
            seen[j]=i