import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k, q = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))

        ans = streak = 0

        for a in arr:
            if a <= q:
                streak += 1
            else:
                streak = 0
            ans += max(0, streak-k+1)

        
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()