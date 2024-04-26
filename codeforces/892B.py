import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))

    ans = 0
    temp = float('inf')
    for i in range(len(arr)-1, -1, -1):
        if i < temp:
            ans += 1
        temp = min(temp, i - arr[i])
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()