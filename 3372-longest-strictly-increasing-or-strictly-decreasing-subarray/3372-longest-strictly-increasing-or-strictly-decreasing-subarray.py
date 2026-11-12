class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec = 0,0
        longest_inc,longest_dec =0,0
        for x in range(1,len(nums)):
            if nums[x-1]<nums[x]:
                inc+=1
                dec=0
            elif nums[x-1]>nums[x]:
                dec+=1
                inc=0
            else:
                inc=0
                dec=0
            longest_inc = max(longest_inc,inc)
            longest_dec = max(longest_dec,dec)
        return max(longest_inc,longest_dec)+1