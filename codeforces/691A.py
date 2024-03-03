import sys

def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    cnt = arr.count(0)
    if (n == 1 and cnt == 0) or (n > 1 and cnt == 1):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()