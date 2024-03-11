import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))

        odds = 0
        for a in arr:
            if a % 2:
                odds += 1
        
        if (odds == 0) or (odds == n and x % 2 == 0) or (x == n and odds % 2 == 0):
            sys.stdout.write("No\n")
        else:
            sys.stdout.write("Yes\n")


if __name__ == "__main__":
    main()