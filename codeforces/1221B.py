import sys


def main():
    n = int(sys.stdin.readline())
    board = [['.' for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                sys.stdout.write("B")
            else:
                sys.stdout.write("W")
        sys.stdout.write("\n")


if __name__ == "__main__":
    main()