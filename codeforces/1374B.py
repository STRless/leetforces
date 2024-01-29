import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())

        ans = 0
        while n != 1:
            if n % 6 == 0:
                n /= 6
                ans += 1
            else:
                if (n*2) % 6 == 0:
                    n *= 2
                    ans += 1
                else:
                    ans = -1
                    break
        sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()