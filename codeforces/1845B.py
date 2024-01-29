import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        ax, ay = map(int, sys.stdin.readline().split())
        bx, by = map(int, sys.stdin.readline().split())
        cx, cy = map(int, sys.stdin.readline().split())

        temp1 = 0
        temp2 = 0
        if by > ay and cy > ay or by < ay and cy < ay:
            temp1 = min(abs(ay-by), abs(ay-cy))
        if bx > ax and cx > ax or bx < ax and cx < ax:
            temp2 = min(abs(ax-bx), abs(ax-cx))
        sys.stdout.write(f"{temp1+temp2+1}\n")


if __name__ == "__main__":
    main()