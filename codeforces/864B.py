import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    check = set()
    ans = 0
    for ch in s:
        if ch.isupper():
            ans = max(ans, len(check))
            check.clear()
        else:
            check.add(ch)
    ans = max(ans, len(check))
    sys.stdout.write(f"{ans}\n")


if __name__ == "__main__":
    main()