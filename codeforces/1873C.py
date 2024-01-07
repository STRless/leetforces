import sys

def get_points(x, y, boundary):
    if x == 0 or x == boundary - 1 or y == 0 or y == boundary - 1:
        return 1
    elif x == 1 or x == boundary - 2 or y == 1 or y == boundary - 2:
        return 2
    elif x == 2 or x == boundary - 3 or y == 2 or y == boundary - 3:
        return 3
    elif x == 3 or x == boundary - 4 or y == 3 or y == boundary - 4:
        return 4
    return 5


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        grid = [sys.stdin.readline().strip() for _ in range(10)]
        boundary = 10

        ans = 0
        for i in range(boundary):
            for j in range(boundary):
                if grid[i][j] == 'X':
                    ans += get_points(i, j, boundary)
        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()