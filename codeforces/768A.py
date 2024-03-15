import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    mi = min(arr)
    ma = max(arr)
    ans = 0
    for a in arr:
        if a > mi and a < ma:
            ans += 1
    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()