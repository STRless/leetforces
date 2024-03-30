import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    streak = 0
    prev = -1
    for i in range(n):
        if arr[i] != prev:
            prev = arr[i]
            streak += 1
            ans = max(ans, streak)
        else:
            prev = arr[i]
            streak = 1
    print(ans)


if __name__ == "__main__":
    main()