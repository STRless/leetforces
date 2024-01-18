class Solution:
    def minOperations(self, s1: str, s2: str, x: int) -> int:
        n = len(s1)
        diff = []
        for i in range(n):
            if s1[i] != s2[i]:
                diff.append(i)
        
        if len(diff) % 2:
            return -1
        
        @cache
        def dfs(i):
            if i == 0:
                return x / 2
            if i == -1:
                return 0
            return min(dfs(i-1) + x/2, dfs(i-2) + diff[i] - diff[i-1])
        return int(dfs(len(diff)-1))