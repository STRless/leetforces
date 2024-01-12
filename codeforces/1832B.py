import sys
import heapq

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))
        arr.sort()
        prefix = [0 for _ in range(n+1)]
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        ans = 0
        for i in range(k+1):
            ans = max(ans, prefix[n-(k-i)] - prefix[2*i])
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()