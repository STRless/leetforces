import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        ans = n-1
        for i in range(n):
            if s[i] == '>' or s[n-1-i] == '<':
                ans = min(ans, i)
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()