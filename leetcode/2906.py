class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        pre = [1 for _ in range(n*m)]
        pre[0] = grid[0][0]
        suff = [1 for _ in range(n*m)]
        suff[-1] = grid[-1][-1]
        check = list(chain.from_iterable(grid))
        for i in range(1, n*m):
            pre[i] = (pre[i-1]*check[i]) % 12345
        for i in range((n*m)-2, -1, -1):
            suff[i] = (suff[i+1]*check[i]) % 12345
        
        ans = [[0 for _ in range(m)] for _ in range(n)]
        
        for i in range(n*m):
            row = i // m
            col = (i % m)
            if i == 0:
                ans[row][col] = suff[1] % 12345
            elif i == (n*m)-1:
                ans[row][col] = pre[-2] % 12345
            else:
                ans[row][col] = (suff[i+1] * pre[i-1]) % 12345
        
        return ans