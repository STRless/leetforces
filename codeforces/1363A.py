import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, x = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))

        odds = evens = 0
        for a in arr:
            if a % 2:
                odds += 1
            else:
                evens += 1
        
        m = min(evens, x-1)
        d = x - m

        if d % 2 == 0:
            d += 1


        if odds >= d and d <= x:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")


if __name__ == "__main__":
    main()