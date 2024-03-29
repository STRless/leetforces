import sys


def main():
    k = int(sys.stdin.readline())
    for _ in range(k):
        n, x, t = map(int, sys.stdin.readline().split())
        temp = t // x
        ans = 0
        lim = max(0, n - temp)
        ans = lim*temp
        temp -= 1
        ans += (temp*temp+temp)//2
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()