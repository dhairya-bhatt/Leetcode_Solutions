class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0
        x = 0
        while x < len(s):
            if x + 1 < len(s) and s[x:x+2] in ["IV", "IX", "XL", "XC", "CD", "CM"]:
                if s[x:x+2] == "IV":
                    number += 4
                elif s[x:x+2] == "IX":
                    number += 9
                elif s[x:x+2] == "XL":
                    number += 40
                elif s[x:x+2] == "XC":
                    number += 90
                elif s[x:x+2] == "CD":
                    number += 400
                elif s[x:x+2] == "CM":
                    number += 900
                x += 2
            else:
                if s[x] == "I":
                    number += 1
                elif s[x] == "V":
                    number += 5
                elif s[x] == "X":
                    number += 10
                elif s[x] == "L":
                    number += 50
                elif s[x] == "C":
                    number += 100
                elif s[x] == "D":
                    number += 500
                elif s[x] == "M":
                    number += 1000
                x += 1
        return number