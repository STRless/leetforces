import sys


def main():
    n, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    flag = True
    small = min(arr)
    ans = 0
    for a in arr:
        if (a-small) % k:
            flag = False
            break
        ans += (a-small) // k
    if not flag:
        sys.stdout.write("-1\n")
        return
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()