import sys


def main():
    n = int(sys.stdin.readline())
    for _ in range(n):
        s = sys.stdin.readline().strip()
        t = sys.stdin.readline().strip()
        i = j = 0
        flag = True
        while i < len(s) and j < len(t):
            if s[i] != t[j]:
                flag = False
                break
            cnt1 = 0
            ch = s[i]
            while i < len(s) and s[i] == ch:
                cnt1 += 1
                i += 1
            ch = t[j]
            cnt2 = 0
            while j < len(t) and t[j] == ch:
                cnt2 += 1
                j += 1
            if cnt1 > cnt2:
                flag = False
                break
        if flag and i == len(s) and j == len(t):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()