class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        ans = float('inf')
        n = len(grid)
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                cost = 0
                ni, nj = 0, 0
                center = n//2
                visit = set()
                while not (ni == center and nj == center):
                    if grid[ni][nj] != i:
                        cost += 1
                    visit.add((ni, nj))
                    ni += 1
                    nj += 1
                ni, nj = 0, n-1
                while not (ni == center and nj == center):
                    if grid[ni][nj] != i:
                        cost += 1
                    visit.add((ni, nj))
                    ni += 1
                    nj -= 1
                ni, nj = n-1, center
                while ni >= center:
                    if grid[ni][nj] != i:
                        cost += 1
                    visit.add((ni, nj))
                    ni -= 1
                for x in range(n):
                    for y in range(n):
                        if (x, y) not in visit and grid[x][y] != j:
                            cost += 1
                ans = min(ans, cost)
        return ans
                
                    
                    