import sys
from collections import deque

def main():
    n = int(sys.stdin.readline())
    cool = list(map(int, sys.stdin.readline().split()))
    cool.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if cool[i] == cool[j]:
                ans += 1
                cool[j] += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()