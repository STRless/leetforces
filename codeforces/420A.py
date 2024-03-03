import sys


def main():
    s = sys.stdin.readline().strip()

    backwards = s[::-1]

    flag = True
    for ch in s:
        if ch in ['B', 'C', 'D', 'E', 'F', 'G', 'J', 'K', 'L', 'N', 'P', 'Q', 'R', 'S', 'Z']:
            flag = False

    if s == backwards and flag:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()