class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        out=[]
        for x in range(len(nums)):
            if nums[x]<=target:
                if nums[x]==target:
                    out.append(x)
            else:
                break
        return out