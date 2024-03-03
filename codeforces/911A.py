import sys


def main():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    min_num = min(arr)
    prev = -1
    ans = float('inf')
    for i, a in enumerate(arr):
        if a == min_num:
            if prev != -1:
                ans = min(ans, i-prev)
            prev = i
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()