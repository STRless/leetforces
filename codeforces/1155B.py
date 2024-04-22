import sys


def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()

    cnt1 = (n-11)//2
    cnt2 = cnt1
    i = 0
    while i < n:
        if s[i] == '8':
            if cnt1:
                cnt1 -= 1
            else:
                break
        else:
            if cnt2:
                cnt2 -= 1
            else:
                break
        i += 1
    if s[i] == "8":
        sys.stdout.write("YES")
    else:
        sys.stdout.write("NO")


if __name__ == "__main__":
    main()
