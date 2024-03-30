import sys
from collections import defaultdict


def main():
    n = int(sys.stdin.readline())
    check = defaultdict(int)
    ans = 0
    for _ in range(n):
        h, m = map(str, sys.stdin.readline().split())
        temp = 'h' + h + 'm' + m
        check[temp] += 1
        ans = max(ans, check[temp])
    
    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()