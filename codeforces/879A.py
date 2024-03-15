import sys


def main():
    n = int(sys.stdin.readline())
    arr = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
    prev = arr[0][0]
    for i in range(1, n):
        cur = arr[i][0]
        temp = 1
        while cur <= prev:
            cur = arr[i][0] + (temp * arr[i][1])
            temp += 1
        prev = cur
    sys.stdout.write(f"{prev}")


if __name__ == "__main__":
    main()