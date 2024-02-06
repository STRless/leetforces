import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        arr = list(map(int, sys.stdin.readline().split()))
        cnt = 0
        for a in arr:
            if a % 2: cnt += 1
        if cnt <= 1:
            sys.stdout.write("YES\n")
        else:
            if arr[0] > 0 and arr[1] > 0 and arr[2] > 0:
                arr[0] -= 1
                arr[1] -= 1
                arr[2] -= 1
                arr[3] += 3
                cnt = 0
                for a in arr:
                    if a % 2: cnt += 1
                if cnt <= 1:
                    sys.stdout.write("YES\n")
                else:
                    sys.stdout.write("NO\n")
            else:
                sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()