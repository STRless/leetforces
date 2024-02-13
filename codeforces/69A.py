import sys


def main():
    n = int(sys.stdin.readline())
    arr = [0, 0, 0]
    for _ in range(n):
        t = list(map(int, sys.stdin.readline().split()))
        arr[0] += t[0]
        arr[1] += t[1]
        arr[2] += t[2]
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()