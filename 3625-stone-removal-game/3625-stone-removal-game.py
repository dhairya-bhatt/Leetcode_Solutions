class Solution:
    def canAliceWin(self, n: int, take: int = 10) -> bool:
        return n>=take and not self.canAliceWin(n-take,take-1)
