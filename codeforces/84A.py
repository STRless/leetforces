import sys


def main():
    n = int(sys.stdin.readline())
    sys.stdout.write(f"{n+(n//2)}")


if __name__ == "__main__":
    main()