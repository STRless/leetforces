import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())

        ans = 0
        while n > 0:
            if n >= k:
                ans += n % k
                n //= k
                ans += 1
            else:
                ans += n
                break
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()