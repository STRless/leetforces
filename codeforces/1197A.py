import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        arr.sort(reverse=True)
        limit = min(arr[0], arr[1])
        cnt = 0
        for a in arr[2:]:
            if cnt == limit-1:
                break
            cnt += 1
        sys.stdout.write(f"{cnt}\n")


if __name__ == "__main__":
    main()