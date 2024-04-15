import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    s = sys.stdin.readline().strip()
    sx = sy = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx = i
                sy = j
    
    choices = []
    visited = [False for _ in range(4)]
    def f(cur=[]):
        if len(cur) == 4:
            choices.append(cur.copy())
        for i in range(4):
            if not visited[i]:
                visited[i] = True
                cur.append(i)
                f()
                cur.pop()
                visited[i] = False
    f()
    ans = 0
    change = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for c in choices:
        x, y = sx, sy
        for ch in s:
            idx = int(ch)
            idx = c[idx]
            x += change[idx][0]
            y += change[idx][1]
            if x >= n or y >= m or x < 0 or y < 0 or grid[x][y] == '#':
                break
            if grid[x][y] == 'E':
                ans += 1
                break
    print(ans)



if __name__ == "__main__":
    main()