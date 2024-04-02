import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    check = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        check[a].append(b)
        check[b].append(a)
    
    cnt = 0
    for key, val in check.items():
        if len(val) == 1:
            cnt += 1
    
    print(cnt)


if __name__ == "__main__":
    main()