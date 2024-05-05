import sys


def main():
    t = int(sys.stdin.readline())

    for i in range(t):
        n, m, k = map(int, sys.stdin.readline().split())
        d = n // k
        a1 = min(m, d)
        a2 = (m - a1 + k - 2) // (k - 1)
        ans = a1-a2
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()