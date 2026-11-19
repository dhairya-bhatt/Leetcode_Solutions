from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        sorted_count = sorted(count, key = count.get)
        return sorted_count[::-1][0:k]