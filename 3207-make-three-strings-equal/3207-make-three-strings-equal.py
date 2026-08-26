class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        count = 0
        for x in range(min(len(s1),len(s2),len(s3))):
            if s1[x] == s2[x]== s3[x]:
                count+=1
            else:
                break
        return len(s1)+len(s2)+len(s3) - 3 * count if count >0 else -1
        