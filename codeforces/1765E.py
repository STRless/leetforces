import sys
import math 


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, a, b = map(int, sys.stdin.readline().split())
        if a <= b:
            sys.stdout.write(f"{math.ceil(n/a)}\n")
        else:
            sys.stdout.write("1\n")


if __name__ == "__main__":
    main()