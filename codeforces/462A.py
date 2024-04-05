import sys


def main():
    n = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    v1 = [0, 0, -1, 1]
    v2 = [-1, 1, 0, 0]
    for i in range(n):
        for j in range(n):
            cnt = 0
            for k in range(4):
                ni, nj = i + v1[k], j + v2[k]
                if ni >= n or nj >= n or ni < 0 or nj < 0:
                    continue
                if grid[ni][nj] == 'o':
                    cnt += 1
            if cnt % 2:
                sys.stdout.write("NO\n")
                return
    sys.stdout.write("YES\n")


if __name__ == "__main__":
    main()