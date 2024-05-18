import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        total = 0
        for a in arr:
            total += abs(a)
        sys.stdout.write(f"{total}\n")


if __name__ == "__main__":
    main()