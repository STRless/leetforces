class Solution:
    def sortVowels(self, s: str) -> str:
        def is_vowel(ch):
            return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
        vowels = [ch for ch in s if is_vowel(ch.lower())]
        vowels.sort()
        ans = list(s)
        j = 0
        for i, a in enumerate(ans):
            if is_vowel(a.lower()):
                ans[i] = vowels[j]
                j += 1
        return "".join(ans)