import sys


def main():
    n, p = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    changed = False
    for i in range(n-p):
        if s[i] == '.' and s[i+p] == '.':
            s[i] = '0'
            s[i+p] = '1'
            changed = True
        elif s[i] == '.':
            if s[i+p] == '0':
                s[i] = '1'
            else:
                s[i] = '0'
            changed = True
        elif s[i+p] == '.':
            changed = True
            if s[i] == '0':
                s[i+p] = '1'
            else:
                s[i+p] = '0'
        elif s[i] != s[i+p]:
            changed = True
    if changed:
        for i in range(n-p, n):
            if s[i] == '.':
                s[i] = '0'
        ans = "".join(s)
        sys.stdout.write(f"{ans}\n")
    else:
        sys.stdout.write("No\n")



if __name__ == "__main__":
    main()