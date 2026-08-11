class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        rec = set()
        for x in nums:
            if x in rec:
                return True
            rec.add(x)
        return False
        