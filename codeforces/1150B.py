import sys


def main():
    n = int(sys.stdin.readline())

    arr = [sys.stdin.readline().strip() for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    def can_fill(x, y):
        if not (0 <= y-1 < n and 0 <= y+1 < n and 0 <= x+2 < n):
            return False
        if arr[x][y] == '.' and arr[x+1][y] == '.' and arr[x+2][y] == '.' and arr[x+1][y-1] == '.' and arr[x+1][y+1] == '.' \
            and not visited[x][y] and not visited[x+1][y] and not visited[x+2][y] and not visited[x+1][y-1] and not visited[x+1][y+1]:
            visited[x][y] = True
            visited[x+1][y] = True
            visited[x+2][y] = True
            visited[x+1][y-1] = True
            visited[x+1][y+1] = True
            return True
        return False

    flag = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] == '.' and not visited[i][j]:
                res = can_fill(i, j)
                flag &= res
    if flag:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()