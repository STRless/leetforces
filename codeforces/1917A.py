import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))

        cur = arr[0]
        for i in range(1, n):
            cur *= arr[i]
        if cur > 0:
            sys.stdout.write("1\n")
            sys.stdout.write("1 0\n")
        else:
            sys.stdout.write("0\n")


if __name__ == "__main__":
    main()