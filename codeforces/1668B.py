import sys, math


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        total = sum(arr)
        min_val = min(arr)
        max_val = max(arr)
        if (n+total-min_val+max_val)<=m:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()