import sys


def main():
    first, last = map(str, sys.stdin.readline().strip().split())
    ans = '!'
    for i in range(1, len(first)+1):
        cur = first[:i]
        for j in range(1, len(last)+1):
            cur += last[:j]
            if cur < ans or ans == '!':
                ans = cur
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()