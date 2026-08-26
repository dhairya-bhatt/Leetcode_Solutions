class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1[0] != s2[0] or s1[0] != s3[0] or s2[0] != s3[0]:
            return -1
        count = 0
        for x in range(min(len(s1),len(s2),len(s3))):
            if s1[x] == s2[x]== s3[x]:
                count+=1
            else:
                break
        return len(s1)+len(s2)+len(s3) - 3 * count
        