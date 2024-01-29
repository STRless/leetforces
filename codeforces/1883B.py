import sys
from collections import Counter

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        cnt = Counter(s)
        odds = 0
        for key, val in cnt.items():
            if val % 2:
                odds += 1
        if odds > k + 1:
            sys.stdout.write("NO\n")
        else:
            sys.stdout.write("YES\n")


if __name__ == "__main__":
    main()


#abab
#aaaaaaaa
#aab