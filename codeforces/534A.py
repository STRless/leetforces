import sys


def main():
    n = int(sys.stdin.readline())
    if n == 1 or n == 2:
        sys.stdout.write("1\n1\n")
    elif n == 3:
        sys.stdout.write("2\n1 3\n")
    else:
        sys.stdout.write(f"{n}\n")
        for i in range(n, 0, -1):
            if i % 2:
                sys.stdout.write(f"{i} ")
        for i in range(n, 0, -1):
            if i % 2 == 0:
                sys.stdout.write(f"{i} ")


if __name__ == "__main__":
    main()