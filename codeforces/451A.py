import sys


def main():
    n, m = map(int, sys.stdin.readline().split())
    if min(n, m) % 2:
        sys.stdout.write("Akshat")
    else:
        sys.stdout.write("Malvika")


if __name__ == "__main__":
    main()