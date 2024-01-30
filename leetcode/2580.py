class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        ranges.sort(key=lambda x: x[0])
        @cache
        def dfs(i=0):
            if i == len(ranges):
                return 1
            
            cur = ranges[i][1]
            j = i+1
            while j < len(ranges) and cur >= ranges[j][0]:
                cur = max(cur, ranges[j][1])
                j += 1
            temp = dfs(j) * 2
            return temp
        
        return dfs() % ((10**9)+7)