import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        res = n//2 + n%2
        sys.stdout.write(f"{res}\n")
        l = 1
        r = 3*n
        while l < r:
            sys.stdout.write(f"{l} {r}\n")
            l += 3
            r -= 3


if __name__ == "__main__":
    main()