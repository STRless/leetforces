class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        cnt = defaultdict(int)
        for word in words:
            temp = [0 for _ in range(52)]
            for i in range(len(word)):
                idx = ord(word[i]) - ord('a')
                if i % 2 == 0:
                    temp[idx] += 1
                else:
                    temp[idx+26] += 1
            cnt[tuple(temp)] += 1
        return len(cnt)
