import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        b = list(map(int, sys.stdin.readline().split()))
        arr = list(zip(a, b))
        arr.sort(key=lambda x: x[0])

        for a, b in arr:
            if k < a:
                break
            k += b
        sys.stdout.write(f"{k}\n")


if __name__ == "__main__":
    main()