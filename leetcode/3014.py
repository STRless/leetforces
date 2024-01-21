class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n
        elif n <= 16:
            remainder = n - 8
            return 8 + (remainder * 2)
        elif n <= 24:
            r2 = n - 16
            return 16+8+(r2*3)
        r3 = n - 24
        return 24+16+8+(r3*4)