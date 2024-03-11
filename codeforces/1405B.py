import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        arr = list(map(int, sys.stdin.readline().split()))
        cnt = temp = 0
        for a in arr:
            if a > 0:
                temp += a
            else:
                if a + temp > 0:
                    temp += a
                else:
                    a += temp
                    cnt -= a
                    temp = 0
        sys.stdout.write(f"{cnt}\n")


if __name__ == "__main__":
    main()