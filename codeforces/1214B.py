import sys


def main():
    b = int(sys.stdin.readline())
    g = int(sys.stdin.readline())
    n = int(sys.stdin.readline())

    ans = 0
    # blues
    for i in range(n+1):
        blue = i
        red = n - i
        if blue <= b and red <= g:
            ans += 1
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()