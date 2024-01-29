import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        if (n%2020<=n//2020):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()