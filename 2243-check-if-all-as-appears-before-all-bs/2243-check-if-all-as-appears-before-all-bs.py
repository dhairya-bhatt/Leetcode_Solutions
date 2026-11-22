class Solution:
    def checkString(self, s: str) -> bool:
        for x in range(len(s)-1):
            if s[x] == 'b' and s[x+1] == 'a':
                return False
        return True