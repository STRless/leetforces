import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()

        check = set()
        ans = 0
        for i in range(n):
            if s[i] not in check:
                check.add(s[i])
                ans += n - i
        sys.stdout.write("{}\n".format(ans))


if __name__ == "__main__":
    main()