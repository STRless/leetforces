import sys


def is_vowel(ch):
    return ch == 'a' or ch == 'e'


def is_consonant(ch):
    return ch == 'b' or ch == 'c' or ch == 'd'


def main():
    t = int(sys.stdin.readline())

    for _ in range(t):
        n = int(sys.stdin.readline())
        s = sys.stdin.readline().strip()
        i = 0
        ans = ""
        ans = []
        while i < n:
            if i + 2 < n and is_consonant(s[i]) and is_vowel(s[i+1]) and is_consonant(s[i+2]):
                ans.append(s[i])
                ans.append(s[i+1])
                if i + 3 < n and is_vowel(s[i+3]):
                    ans.append('.')
                    i += 2
                elif i + 3 == n:
                    ans.append(s[i+2])
                    i += 3
                else:
                    ans.append(s[i+2])
                    ans.append('.')
                    i += 3
            else:
                ans.append(s[i])
                if i + 1 < n:
                    ans.append(s[i+1])
                i += 2
        sys.stdout.write("{}\n".format("".join(ans)))


if __name__ == "__main__":
    main()