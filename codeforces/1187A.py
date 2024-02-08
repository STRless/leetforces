import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, s, t = map(int, sys.stdin.readline().split())
        res = max((n-s), (n-t))+1
        sys.stdout.write(f"{res}\n")


if __name__ == "__main__":
    main()