import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    cnt = defaultdict(int)
    for i in range(n):
        cnt[grid[i]] += 1
    
    
    ans = 0
    for key, val in cnt.items():
        ans = max(ans, val)
    sys.stdout.write(f"{ans}\n")




if __name__ == "__main__":
    main()