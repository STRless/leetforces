class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        check = defaultdict(int)
        n = len(grid)
        for i in range(n):
            res = "".join(str(grid[i]))
            check[res] += 1
        ans = 0
        for j in range(n):
            temp = []
            for i in range(n):
                temp.append(grid[i][j])
            res = "".join(str(temp))
            ans += check[res]
        return ans