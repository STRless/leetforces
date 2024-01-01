import sys
from collections import deque

# Topics: Graph, BFS
# Time Complexity: O(nm)
# Space Complexity: O(nm)


def create_walls(grid, n, m):
    v1 = [0, 0, -1, 1]
    v2 = [-1, 1, 0, 0]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                for k in range(4):
                    x, y = i + v1[k], j + v2[k]
                    if 0 <= x < n and 0 <= y < m and grid[x][y] == '.':
                        grid[x][y] = '#'


def person_can_escape(grid, visited, n, m, x, y):
    v1 = [0, 0, -1, 1]
    v2 = [-1, 1, 0, 0]
    visited[x][y] = True
    q = deque()
    q.append((x, y))
    while q:
        ox, oy = q.popleft()
        for i in range(4):
            nx, ny = ox + v1[i], oy + v2[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#' and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        grid = [list(sys.stdin.readline().strip()) for _ in range(n)]

        create_walls(grid, n, m)

        visited = [[False for _ in range(m)] for _ in range(n)]
        if grid[n-1][m-1] == '.':
            person_can_escape(grid, visited, n, m, n-1, m-1)

        flag = True
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'G' and not visited[i][j]:
                    flag = False
                if grid[i][j] == 'B' and visited[i][j]:
                    flag = False

        if flag:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")


if __name__ == "__main__":
    main()