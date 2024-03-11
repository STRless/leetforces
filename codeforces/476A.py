import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    lower = (n+1)//2
    ans = (lower+m-1)//m*m
    if ans > n:
        sys.stdout.write("-1")
    else:
        sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()