import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        ans = 0
        for i in range(1, ((n-1)//2)+1):
            ans += (i*i)
        ans *= 8
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()