class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        sort_cnt = []
        for key, val in cnt.items():
            sort_cnt.append((key, val))
        sort_cnt.sort(key=lambda x: -x[1])
        ans = 0
        size=0
        mul = 1
        for a, b in sort_cnt:
            size += 1
            ans += (mul * b)
            if size % 8 == 0:
                size = 0
                mul += 1
        return ans
            