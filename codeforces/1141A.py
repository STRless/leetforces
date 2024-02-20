import sys


def main():
    n, m = map(int, sys.stdin.readline().split())

    ans = -1
    if m % n == 0:
        d = m // n
        ans = 0
        while d % 2 == 0:
            d //= 2
            ans += 1
        while d % 3 == 0:
            d //= 3
            ans += 1
        
        if d != 1:
            ans = -1

    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()