import sys

def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        x, n, m = map(int, sys.stdin.readline().split())

        while x >= 20 and n > 0:
            x = (x//2) + 10
            n -= 1
        
        if m * 10 >= x:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()