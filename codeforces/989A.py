import sys


def main():
    s = sys.stdin.readline().strip()
    for i in range(len(s)-2):
        check = set()
        check.add(s[i])
        check.add(s[i+1])
        check.add(s[i+2])
        if 'A' in check and 'B' in check and 'C' in check:
            sys.stdout.write("Yes\n")
            return
    sys.stdout.write("No\n")


if __name__ == "__main__":
    main()