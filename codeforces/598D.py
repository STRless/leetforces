import sys
from collections import deque

# Topics: Graph, BFS
# Time Complexity: O(nm+k) due to caching results no cell is ever visited twice
# Space Complexity: O(nm)


def bfs(grid, visited, i, x, y, n, m):
    q = deque()
    q.append((x, y))
    visited[x][y] = i
    v1 = [-1, 1, 0, 0]
    v2 = [0, 0, -1, 1]
    cnt = 0
    while q:
        ox, oy = q.popleft()
        for k in range(4):
            nx, ny = ox + v1[k], oy + v2[k]
            if nx >= n or ny >= m or nx < 0 or ny < 0 or visited[nx][ny]:
                continue
            if grid[nx][ny] == '*':
                cnt += 1
                continue
            elif grid[nx][ny] == '*':
                continue
            visited[nx][ny] = i
            q.append((nx, ny))
            
    return cnt


def main():
    n, m, k = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]

    visited = [[0 for _ in range(m)] for _ in range(n)]

    cache = {}

    for i in range(1, k+1):
        x, y = map(int, sys.stdin.readline().split())
        x -= 1
        y -= 1
        if not visited[x][y]:
            cnt = bfs(grid, visited, i, x, y, n, m)
            cache[i] = cnt
            sys.stdout.write("{}\n".format(cnt))
        else:
            sys.stdout.write("{}\n".format(cache[visited[x][y]]))


if __name__ == "__main__":
    main()