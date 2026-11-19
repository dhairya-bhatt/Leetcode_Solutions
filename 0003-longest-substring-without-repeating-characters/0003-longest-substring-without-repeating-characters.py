class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r,longest=0,0,0
        unique = set()
        for x in range(len(s)):
            r+=1
            while s[x] in unique:
                unique.remove(s[l])
                l+=1
            unique.add(s[x])
            longest = max(longest,r-l)
        return longest
                
