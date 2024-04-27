import sys
from collections import deque


def main():
    r, c = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(r)]

    visited = set()

    ans = 0
    v1 = [0, 0, -1, 1]
    v2 = [-1, 1, 0, 0]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'B' and (i, j) not in visited:
                q = deque()
                q.append((i, j))
                visited.add((i, j))
                ans += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + v1[k], y + v2[k]
                        if nx >= r or ny >= c or nx < 0 or ny < 0 or grid[nx][ny] == '.' or (nx, ny) in visited:
                            continue
                        visited.add((nx, ny))
                        q.append((nx, ny))
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()