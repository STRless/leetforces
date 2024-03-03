import sys


def main():
    n, x = map(int, sys.stdin.readline().split())
    ans = 0
    for i in range(1, n+1):
        if x % i == 0 and x // i <= n:
            ans += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()