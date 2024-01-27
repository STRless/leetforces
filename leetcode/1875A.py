import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        a, b, n = map(int, sys.stdin.readline().split())
        arr = list(map(int, sys.stdin.readline().split()))

        arr.sort()
        ans = 0
        for i, num in enumerate(arr):
            if b + num > a:
                ans += b - 1
                b = min(a, num+1)
            else:
                b += num
        ans += b
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()