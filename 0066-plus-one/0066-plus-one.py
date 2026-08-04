class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = int("".join(map(str, digits)))
        num = int(number)
        num += 1
        numbers = str(num)
        ans = []
        for x in numbers:
            ans.append(int(x))
        return ans
        