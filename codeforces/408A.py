import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = float('inf')
    for _ in range(n):
        temp = list(map(int, sys.stdin.readline().split()))
        ans = min(ans, sum(temp) * 5 + len(temp) * 15)
    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()