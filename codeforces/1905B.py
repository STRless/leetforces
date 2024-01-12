import sys
from collections import defaultdict

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        adj = defaultdict(list)
        for _ in range(n-1):
            u, v = map(int, sys.stdin.readline().split())
            adj[u].append(v)
            adj[v].append(u)
        
        cnt = 0
        for i in range(1, n+1):
            if len(adj[i]) == 1:
                cnt += 1

        sys.stdout.write(f"{(cnt+1)//2}\n")


if __name__ == "__main__":
    main()