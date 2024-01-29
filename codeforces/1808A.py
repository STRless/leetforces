import sys


def main():
    t = int(sys.stdin.readline())
    cache = {}
    for _ in range(t):
        l, r = map(int, sys.stdin.readline().split())
        if r - l >= 100:
            while r >= l:
                temp = str(r)
                if temp[-1] == '0' and temp[-2] == '9':
                    break
                r -= 1
            sys.stdout.write(f"{r}\n")
        else:
            check = ""
            ans = -1
            while l <= r:
                temp = str(l)
                big = 0
                small = 10
                for ch in temp:
                    small = min(small, int(ch))
                    big = max(big, int(ch))
                if big - small > ans:
                    ans = big-small
                    check = temp
                l += 1
            sys.stdout.write(f"{check}\n")


if __name__ == "__main__":
    main()