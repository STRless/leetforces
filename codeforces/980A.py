import sys

def main():
    s = sys.stdin.readline().strip()
    link = pearl = 0
    for ch in s:
        if ch == 'o':
            pearl += 1
        else:
            link += 1
    if pearl == 0 or link == 0 or (link >= pearl and link % pearl == 0):
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()