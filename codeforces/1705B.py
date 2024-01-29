import sys


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        ptr = 0
        ans = 0
        for i in range(n):
            if arr[i] != 0:
                break
            ptr += 1
        
        for i in range(ptr, n-1):
            ans += arr[i]
            if arr[i] == 0:
                ans += 1
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()