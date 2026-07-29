class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        
        sign = 1
        if s[0] in "+-":
            if s[0] == "-":
                sign = -1
            s = s[1:]
            
        final_word = ""
        for x in range(len(s)):
            if s[x].isdigit() == True:
                final_word += s[x]
            else:
                break
        if not final_word:
            return 0
        
        output = sign * int(final_word)
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        output = max(min(output, INT_MAX), INT_MIN)

        return output
