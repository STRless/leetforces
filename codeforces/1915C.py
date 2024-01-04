import sys
import math

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        total = sum(list(map(int, sys.stdin.readline().split())))

        temp = int(math.sqrt(total))
        if temp * temp == total:
            sys.stdout.write("Yes\n")
        else:
            sys.stdout.write("No\n")


if __name__ == "__main__":
    main()