import sys
from functools import cache

sys.setrecursionlimit(10**5)

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    avail = set(sys.stdin.readline().split())

    dp = [0 for _ in range(n)]
    for i in range(n-1, -1, -1):
        if i + 1 == n and s[i] in avail:
            dp[i] = 1
        elif s[i] in avail:
            dp[i] += dp[i+1] + 1
    
    sys.stdout.write("{}".format(sum(dp)))


if __name__ == "__main__":
    main()