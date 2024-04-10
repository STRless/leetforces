import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = -1
    deq = deque()
    for i, a in enumerate(arr):
        deq.append((i+1, a))
    
    while deq:
        idx, amt = deq.popleft()
        ans = idx
        if amt > m:
            amt -= m
            deq.append((idx, amt))


    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()