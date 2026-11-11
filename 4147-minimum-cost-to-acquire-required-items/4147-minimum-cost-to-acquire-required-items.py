class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        combined_min = min(costBoth,cost1+cost2) * min(need1,need2)
        rest1 = min(costBoth,cost1) * (need1-min(need1,need2))
        rest2 = min(costBoth,cost2) * (need2-min(need1,need2))
        return combined_min+rest1+rest2