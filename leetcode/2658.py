class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ans = 0
        n, m = len(grid), len(grid[0])
        visit = set()
        def bfs(x, y):
            v1 = [0, 0, -1, 1]
            v2 = [-1, 1, 0, 0]
            visit.add((x, y))
            temp = grid[x][y]
            q = deque()
            q.append((x, y))
            while q:
                ox, oy = q.popleft()
                for i in range(4):
                    nx, ny = ox + v1[i], oy + v2[i]
                    if nx >= n or ny >= m or nx < 0 or ny < 0 or grid[nx][ny] == 0 or (nx, ny) in visit:
                        continue
                    q.append((nx, ny))
                    visit.add((nx, ny))
                    temp += grid[nx][ny]
            return temp
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0 and (i, j) not in visit:
                    ans = max(ans, bfs(i, j))
        return ans
                    