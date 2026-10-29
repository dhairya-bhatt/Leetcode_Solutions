class Solution:
    def minimumPairRemoval(self, a: List[int]) -> int:
        return sum(a>sorted(a)!=[a:=a[:i]+[s]+a[i+2:]for s,i in[min(zip(map(add,a,a[1:]),count()))]]for _ in a)