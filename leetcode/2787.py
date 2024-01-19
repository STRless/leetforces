class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        @cache
        def dfs(remains=n, num=1):
            if remains < 0:
                return 0
            if remains == 0:
                return 1
            if num**x > remains:
                return 0
            
            temp = num**x

            op1 = dfs(remains-temp, num+1)
            op2 = dfs(remains, num+1)
            return op1+op2
        return dfs() % (10**9+7)