import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        s = sys.stdin.readline().strip()

        i = 0
        cnt = 0
        while i < n:
            if s[i] == 'B':
                i += k
                cnt += 1
            else:
                i += 1
        sys.stdout.write("{}\n".format(cnt))


if __name__ == "__main__":
    main()