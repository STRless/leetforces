import sys
from collections import deque

def main():
    n, k = map(int, sys.stdin.readline().split())
    pows = deque(map(int, sys.stdin.readline().split()))

    if k >= n-1:
        # its the max
        ans = max(pows)
        sys.stdout.write(f"{ans}\n")
    else:
        streak = 0
        prev = -1
        while True:
            num1, num2 = pows.popleft(), pows.popleft()
            if prev == -1:
                prev = max(num1, num2)
                streak = 1
            else:
                if prev == max(num1, num2):
                    streak += 1
                else:
                    prev = max(num1, num2)
                    streak = 1
            pows.appendleft(max(num1, num2))
            pows.append(min(num1, num2))
            if streak == k:
                break
        sys.stdout.write(f"{prev}\n")


if __name__ == "__main__":
    main()