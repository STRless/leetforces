import sys


def main():
    s = sys.stdin.readline().strip()
    t = sys.stdin.readline().strip()

    def is_vowel(ch):
        return ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'
    
    if len(s) != len(t):
        sys.stdout.write("No\n")
    else:
        for i in range(len(s)):
            flag1 = is_vowel(s[i])
            flag2 = is_vowel(t[i])
            if flag1 != flag2:
                sys.stdout.write("No\n")
                return
        sys.stdout.write("Yes\n")


if __name__ == "__main__":
    main()