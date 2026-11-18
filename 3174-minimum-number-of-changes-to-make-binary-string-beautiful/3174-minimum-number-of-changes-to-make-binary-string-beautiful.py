class Solution:
    def minChanges(self, s: str) -> int:
        counter = 0
        for x in range(0,len(s),2):
            if s[x]!=s[x+1]:
                counter+=1
        return counter
