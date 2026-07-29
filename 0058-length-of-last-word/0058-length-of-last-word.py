class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s0 = s.strip()
        word_array = s0.split(" ")
        last = len(word_array)
        return len(word_array[last-1])