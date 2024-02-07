import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    cafes = list(map(int, sys.stdin.readline().split()))
    check = defaultdict(int)
    for i, cafe in enumerate(cafes):
        check[cafe] = i
    
    ans = -1
    temp = float('inf')
    for key, val in check.items():
        if val < temp:
            temp = val
            ans = key
    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()