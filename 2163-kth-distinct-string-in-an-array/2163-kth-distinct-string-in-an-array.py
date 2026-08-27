class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        non_repeating = [item for item in arr if arr.count(item) == 1]
        if k>len(non_repeating):
            return ""
        else:
            return non_repeating[k-1]