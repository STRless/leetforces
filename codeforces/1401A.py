import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        if n < k:
            res = k-n
            sys.stdout.write(f"{res}\n")
        elif n%2 == k%2:
            sys.stdout.write(f"{0}\n")
        else:
            sys.stdout.write(f"{1}\n")


if __name__ == "__main__":
    main()