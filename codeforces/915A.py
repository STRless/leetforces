import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    ans = 0

    for a in arr:
        if k % a == 0:
            ans = max(ans, a)
    ans = k // ans
    sys.stdout.write(f"{ans}")

if __name__ == "__main__":
    main()
