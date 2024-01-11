class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        def isVowel(ch):
            return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
        for i in range(n):
            v = c = 0
            for j in range(i, n):
                if isVowel(s[j]):
                    v += 1
                else:
                    c += 1
                if v == c and (v * c) % k == 0:
                    ans += 1
        return ans