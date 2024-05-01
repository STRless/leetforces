import sys


def is_vowel(ch):
    return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'y'


def main():
    n = int(sys.stdin.readline())
    patterns = list(map(int, sys.stdin.readline().split()))
    flag = True
    for i in range(n):
        s = sys.stdin.readline().strip()
        cnt = 0
        for ch in s:
            if is_vowel(ch):
                cnt += 1
        if cnt != patterns[i]:
            flag = False
    if flag:
        sys.stdout.write("YES\n")
    else:
        sys.stdout.write("NO\n")


if __name__ == "__main__":
    main()