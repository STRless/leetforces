import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    counter = set(arr)
    if len(counter) == 1 or len(counter) == 2:
        sys.stdout.write("YES\n")
    elif len(counter) == 3:
        arr = list(counter)
        arr.sort()
        if arr[1] - arr[0] == arr[2] - arr[1]:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()