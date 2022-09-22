class Solution:
    def reverseWords(self, s: str) -> str:
        reversed = ""
        words = s.split()
        for iter, word in enumerate(words):
            reversed += word[::-1] + " "
        return reversed[:-1]