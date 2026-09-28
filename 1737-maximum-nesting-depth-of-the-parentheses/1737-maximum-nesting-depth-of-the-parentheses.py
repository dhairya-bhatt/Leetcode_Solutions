class Solution:
    def maxDepth(self, s: str) -> int:
        maxi=0
        result = 0
        for char in s:
            if char == "(":
                maxi+=1
            elif char == ")":
                result = max(result, maxi)
                maxi-=1
        return result
