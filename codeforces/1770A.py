import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, m = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        a.sort()
        b.sort(reverse=True)

        ans = 0
        for i in range(n):
            if i >= m:
                break
            ans += b[i]
        if n > m:
            ans += sum(a[m:])
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()