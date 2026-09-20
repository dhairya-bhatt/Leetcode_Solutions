class Solution:
    def reverseDegree(self, s: str) -> int:
        sum,i=0,1
        for char in s:
            sum+= (123-ord(char))*i
            i+=1
        return sum