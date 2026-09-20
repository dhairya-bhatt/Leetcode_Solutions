class Solution:
    def reverseDegree(self, s: str) -> int:
        sum=0
        i=1
        for char in s:
            sum+= (26-(ord(char)-97))*i
            i+=1
            print(sum)
        return sum