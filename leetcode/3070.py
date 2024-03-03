class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        ans = 0
        row, col = len(grid), len(grid[0])
        pre = [[0 for _ in range(col)] for _ in range(row)]
        row_sums = [[0 for _ in range(col)] for _ in range(row)]
        for j in range(col):
            for i in range(row):
                if i - 1 >= 0:
                    row_sums[i][j] += row_sums[i-1][j]
                row_sums[i][j] += grid[i][j]
        for i in range(row):
            for j in range(col):
                cur = grid[i][j]
                if i - 1 >= 0 and j - 1 >= 0:
                    pre[i][j] += pre[i][j-1]
                    pre[i][j] += row_sums[i-1][j]
                elif i - 1 >= 0:
                    pre[i][j] += pre[i-1][j]
                elif j - 1 >= 0:
                    pre[i][j] += pre[i][j-1]
                pre[i][j] += cur
                if pre[i][j] <= k:
                    ans += 1
        return ans