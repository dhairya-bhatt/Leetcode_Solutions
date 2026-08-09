import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowerS = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return lowerS == lowerS[::-1]