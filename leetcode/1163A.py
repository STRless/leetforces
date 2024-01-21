import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    ans = min(m, n-m) if m else 1
    sys.stdout.write(f"{ans}")


if __name__ == "__main__":
    main()