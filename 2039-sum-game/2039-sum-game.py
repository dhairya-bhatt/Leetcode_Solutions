class Solution:
    def sumGame(self, num: str) -> bool:
        hf = int(len(num))//2
        s1,s2=num[:hf],num[hf:]
        q1 = s1.count("?")
        q2 = s2.count("?")
        sum1 = sum(int(char) for char in s1 if char.isdigit())
        sum2 = sum(int(char) for char in s2 if char.isdigit())
        return (sum1 - sum2) * 2 != (q2 - q1) * 9
                