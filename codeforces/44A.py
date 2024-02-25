import sys


def main():
    n = int(sys.stdin.readline())
    check = {}
    for _ in range(n):
        a, b = map(str, sys.stdin.readline().split())
        key = a + "#" + b
        check[key] = 0
    sys.stdout.write(f"{len(check)}")


if __name__ == "__main__":
    main()