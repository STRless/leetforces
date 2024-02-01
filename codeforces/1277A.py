import sys
from collections import Counter


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        ans = 0
        for i in range(1, 10):
            ch = str(i)
            cur = ch
            while int(cur) <= n:
                ans += 1
                cur += ch
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()
