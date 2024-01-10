class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        i, ans = 1, 0
        while i < len(word):
            if word[i] == word[i-1] or abs(ord(word[i])-ord(word[i-1])) == 1:
                ans += 1
                i += 2
            else:
                i += 1
        return ans