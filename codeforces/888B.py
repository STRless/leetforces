import sys


def main():
    n = int(sys.stdin.readline())
    dir = sys.stdin.readline().strip()

    x = y = 0
    for i, ch in enumerate(dir):
        if ch == 'D':
            y += 1
        elif ch == 'U':
            y -= 1
        elif ch == 'L':
            x -= 1
        else:
            x += 1

    print(n - abs(x) - abs(y))


if __name__ == "__main__":
    main()