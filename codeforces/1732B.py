import sys


def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        prev = '!'
        cnt = 0
        for ch in s:
            if ch != prev:
                prev = ch
                cnt += 1
        if s[0] == '0' and cnt > 1:
            sys.stdout.write(f"{cnt-2}\n")
        else:
            sys.stdout.write(f"{cnt-1}\n")


if __name__ == "__main__":
    main()